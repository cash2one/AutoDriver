# coding=utf-8
__author__ = 'guohai@live.com'

import os
import xlrd
import re


class Excel:
    #skip_cat 是否读取cat详细数据
    #dict_header excel表头的中文对应到英文命名
    def __init__(self, file_name,dict_header,skip_cat):
        self.file = file_name
        self.skip_cat = skip_cat
        self.dict_header = dict_header

    # 打开excel
    def openExcel(self):
        try:
            return xlrd.open_workbook(self.file)
        except Exception:
            #print str(e)
            print u'excel文件不存在,请查看config.ini的配置，或查看excel目录是否有对应文件存在！'
            return None

    # 根据表名获取列表内容
    def readByName(self, col_index, sheet_name):
        book = self.openExcel()
        sheet = book.sheet_by_name(sheet_name)
        #sheet.cell_value(rowx=0,colx=1)
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

    # def readByTitleName(self,tup,sheet_index):
    #     data = self.openExcel()
    #
    #     list = []
    #     col_indexs=self.findIndexByName(data,tup)
    #     p = re.compile(r'(?<=\{).*?(?=})')
    #     tables = data.sheets()
    #     for t in tables:
    #         nrows = t.nrows
    #         for r in range(1,nrows):
    #             for c in col_indexs:
    #                 match=p.search(t.row_values(r)[c])
    #                 if match:
    #                     print jsons.find_jsons(match.group())
    #                 else:
    #                     print t.row_values(r)[c]

    #根据setting.cfg 过滤excel用例的列
    def filterRows(self,titles,one_row_vals):
        titlea=[]
        rows=[]

        for i in range(0,len(titles)):
            settings_vals = self.dict_header.values()
            if titles[i] in settings_vals:

               for k,v in self.dict_header.items():
                   if v == titles[i]:
                      titlea.append(k)
                      break

               rows.append(one_row_vals[i])

        return titlea,rows


    #取出行内符合条件的单元格内容
    def getCellsAllValue(self,one_row_vals,new_header,sheet_index):
        #url = self.getExcelSettings('interface_url')['url']
        cells={}

        if one_row_vals:
            for i in range(len(new_header)):#遍历表头
                k = new_header[i]
                if k=='desc' and one_row_vals[i-1]!='begin':
                    cells[k] = one_row_vals[i]
                elif k=='script':
                    if one_row_vals[i].strip()=='':
                        cells[k] = ''
                    else:
                        cells[k] = one_row_vals[i].replace('.py','')
                elif k=='exp': #去除exp中的token
                    # exp_val = self.getTokenStr(one_row_vals[i])
                    # if exp_val != None:
                    #     cells[k] = one_row_vals[i].replace(exp_val,'')
                    # else:
                    #     cells[k] = one_row_vals[i]
                    if '[0]' in one_row_vals[i]:#区分list为空和不为空
                        cells[k] = one_row_vals[i].replace('[0]','[]')
                    else:
                        cells[k] = one_row_vals[i]
                elif k == 'no':
                    row_no =str(sheet_index)+'_'+str(self.floatToInt(one_row_vals[i]))
                    cells[k]=row_no
                elif k == 'loop':
                    cells[k]=self.floatToInt(one_row_vals[i])
                else:
                    cells[k] = one_row_vals[i]

                #用例描述里面正则取接口地址
                # if header[i] == xls_settings['desc']:
                #     cells[k] = self.getInfValue(one_row_vals[i])
                # else:
                #     cells[k] = one_row_vals[i]
            return cells


    #取出行内符合条件的单元格内容
    def getCellsValue(self,one_row_vals,new_header,sheet_index):
        #url = self.getExcelSettings('interface_url')['url']
        cells={}

        if one_row_vals:
            for i in range(len(new_header)):#遍历表头
                k = new_header[i]
                if k=='desc' and one_row_vals[i-1]!='begin':
                    cells[k] = one_row_vals[i]
                elif k=='script':
                    if one_row_vals[i].strip()=='':
                        cells[k] = ''
                    else:
                        cells[k] = one_row_vals[i].replace('.py','')
                elif k=='exp': #去除exp中的token
                    # exp_val = self.getTokenStr(one_row_vals[i])
                    # if exp_val != None:
                    #     cells[k] = one_row_vals[i].replace(exp_val,'')
                    # else:
                    #     cells[k] = one_row_vals[i]
                    if '[0]' in one_row_vals[i]:#区分list为空和不为空
                        cells[k] = one_row_vals[i].replace('[0]','[]')
                    else:
                        cells[k] = one_row_vals[i]
                elif k=='cat':
                    if not self.skip_cat:
                        cat_filename = os.path.basename(self.file).replace('.xls','')
                        #对该单元格内不为begin、end的内容，为空
                        if one_row_vals[i]=='begin':
                            cells[k] = cat_filename + '_begin'
                        elif one_row_vals[i]=='end':
                            cells[k] = cat_filename + '_end'
                        else:
                            cells[k] = cat_filename
                    else:
                        cells[k] = one_row_vals[i]

                elif k == 'no':
                    row_no =str(sheet_index)+'_'+str(self.floatToInt(one_row_vals[i]))
                    cells[k]=row_no
                elif k == 'loop':
                    cells[k]=self.floatToInt(one_row_vals[i])
                else:
                    cells[k] = one_row_vals[i]

                #用例描述里面正则取接口地址
                # if header[i] == xls_settings['desc']:
                #     cells[k] = self.getInfValue(one_row_vals[i])
                # else:
                #     cells[k] = one_row_vals[i]
            return cells

    def getTokenStr(self,content):
        re_symbol = re.compile(r'(?<=\"tokenNo\"\:\").*?(?=\")')#接口正则
        match=re_symbol.search(content)

        if match:
            return match.group()

    def floatToInt(self,val):
        if not str(val).strip():
            new_val = 0
        else:
            new_val = val
        return int(new_val)


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

