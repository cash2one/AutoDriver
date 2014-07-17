# coding=utf-8
__author__ = 'guohai@live.com'

import os
import files
import xlrd
import re
import jsons
import json

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Excel:

    def __init__(self, file_name):
        self.file = file_name

    # 打开excel
    def openExcel(self):
        try:
            return xlrd.open_workbook(self.file)
        except Exception, e:
            print str(e)

    # 根据表名获取列表内容
    '''
    gewgwwe/** */
    '''
    def readByName(self, col_index, sheet_name):
        book = self.openExcel()
        sheet = book.sheet_by_name(sheet_name)
        sheet.cell_value(rowx=0,colx=1)
        rows = sheet.nrows
        col_names = sheet.row_values(col_index)  # 某一行数据
        list = []
        for num in range(1, rows):
            row = sheet.row_values(num)
            if row:
                app = {}
                for i in range(len(col_names)):
                    app[col_names[i]] = row[i]

                list.append(app)
        return list

    # 根据行列索引值获取内容
    def readByIndex(self, header_index, sheet_index):
        data = self.openExcel()
        table = data.sheets()[sheet_index]
        nrows = table.nrows  # 行数
        cols = table.ncols  # 列数
        col_names = table.row_values(header_index)
        list = []
        for num in range(1, nrows):
            row = table.row_values(num)
            if row:
                app = {}
                for i in range(len(col_names)):#元组遍历
                    #if not type(row[i]) is types.FloatType:
                    app[col_names[i]] = row[i]#.decode('ascii') 放入到app
                list.append(app)
        return list

    def readByTitleName(self,tup,sheet_index):
        data = self.openExcel()

        list = []
        col_indexs=self.findIndexByName(data,tup)
        p = re.compile(r'(?<=\{).*?(?=})')
        tables = data.sheets()
        for t in tables:
            nrows = t.nrows
            for r in range(1,nrows):
                for c in col_indexs:
                    match=p.search(t.row_values(r)[c])
                    if match:
                        print jsons.find_jsons(match.group())
                    else:
                        print t.row_values(r)[c]


    def readTestCaseByConf(self):
        data = self.openExcel()
        sheet = data.sheets()
        xls_settings=self.getExcelSettings('excel')
        #print xls_settings.keys()

        titles = sheet[0].row_values(0)#excel表头

        list = []

        for s in sheet:#遍历所有Sheet
            for n in range(1, s.nrows):#遍历所有行
                new_titles,new_rows=self.filterRows(titles,s.row_values(n),xls_settings)
                app=self.getCellsValue(xls_settings,new_rows,new_titles)
                #self.getCellsValue1(t.row_values(n),titles,tup)
                if app:
                    list.append(app)
        return list

    #根据setting.cfg 过滤excel用例的列
    def filterRows(self,titles,one_row_vals,xls_settings):
        titlea=[]
        rows=[]

        for i in range(0,len(titles)):
            settings_vals = xls_settings.values()
            if titles[i] in settings_vals:
               titlea.append(titles[i])
               rows.append(one_row_vals[i])

        return titlea,rows

    #读取settings.cfg 到list
    def getExcelSettings(self,selections):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        return files.readConfigs(PATH('../config/settings.cfg'),selections)


    #取出行内符合条件的单元格内容
    def getCellsValue(self,xls_settings,one_row_vals,header):
        cells={}
        # scripts=[]
        # expts=[]
        if one_row_vals:
            for i in range(len(header)):#遍历表头
                #if not type(row[i]) is types.FloatType:
                k=self.getKeyByValue(xls_settings,header[i])#取出value相等的key
                cells[k] = one_row_vals[i]

                #用例描述里面正则取接口地址
                # if header[i] == xls_settings['desc']:
                #     cells[k] = self.getInfValue(one_row_vals[i])
                # else:
                #     cells[k] = one_row_vals[i]
            return cells

    #根据value获取list的key
    def getKeyByValue(self,xls_settings,header_cell_val):
        for k,v in xls_settings.items():
            if v==header_cell_val:
               return k


    #正则取出包含在{{}}内的地址，并验证是否是网址
    def getInfValue(self,content):
        re_symbol = re.compile(r'(?<=\{\{).*?(?=}})')#接口正则
        match=re_symbol.search(content)

        if match:
            return match.group()
            #return m
            # try:
            #    x=json.loads(m)
            # except ValueError:
            #     return ''
            #
            # return x

        else:
            return ''

    #读取脚本名和执行次数
    def readScriptLoop(self):
        tup=(u'用例脚本',u'执行次数')
        keys=('script','loop')
        data = self.openExcel()
        list = []
        col_indexs=self.findIndexByName(data,tup)
        tables = data.sheets()
        for t in tables:
            nrows = t.nrows
            for r in range(1,nrows):
                for c in col_indexs:
                    print t.row_values(r)[c]


    #查找字段所在列的引
    def findIndexByName(self,data,tup):
        table=data.sheets()[0]
        cols = table.ncols  # 列数
        col_indexs=[]
        firstRow=table.row_values(0)
        for num in range(0, cols):
            for i in range(len(tup)):#遍历tup
                if firstRow[num]==tup[i]:
                    col_indexs.append(num)
        return col_indexs


def mergeGroup(json_value):
    kw= files.readConfigs(PATH('../config/settings.cfg'),'excel_keyword')
    temp=[]

    isGroup = False
    temp1={}
    isBegin = False

    for jv in json_value:
        if jv['cat'] == kw['begin']:
            isBegin = True
        elif jv['cat'] == kw['end']:
            isBegin = False

        if isBegin:
            if len(temp1)<=0:
                temp1 = jv
            temp1['exp']+=jv['exp']+'|'
            temp1['desc']+=jv['desc']+'|'
        else:
            if len(temp1) > 0:
                temp.append(temp1)
            temp1=jv

    return temp


def main():
    pass


if __name__ == "__main__":
    main()

