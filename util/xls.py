# coding=utf-8
__author__ = 'guohai@live.com'

import os
import files
import xlrd
import re
import jsons

EXCEL_HEADER = (u'用例编号',u'分类',u'用例描述',u'期望结果',u'执行次数')
DESC=u'用例描述'
HEADER = ('no','cat','desc','exp','loop')
INTERFACE='interface'

XLS_HEADER={'no':u'用例编号','cat':u'分类','name':u'用例名','desc':u'用例描述','exp':u'期望结果','script':u'用例脚本','loop':u'执行次数'}

class Excel:

    def __init__(self, file_name):
        self.file = file_name

    # 打开excel
    def openExcel(self):
        try:
            return xlrd.open_workbook(self.file)
        except Exception, e:
            print str(e)


    def getXlsHeader(self,interfaceStr):
        dict_xls = XLS_HEADER
        if interfaceStr!=INTERFACE:
            del dict_xls['desc']
        return dict_xls


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
        #table = data.sheets()[sheet_index]
        #nrows = table.nrows  # 行数
        #cols = table.ncols  # 列数
        #col_names = table.row_values(0)
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
                    #print filter(test.search, t.row_values(r)[c])

    def readTestCaseConf(self,inf=''):
        data = self.openExcel()
        if inf=='interface':
            tup=(u'用例编号',u'分类',u'用例描述',u'期望结果',u'执行次数')
        else:
            tup=(u'用例编号',u'分类',u'用例脚本',u'执行次数')

        xdict = self.getXlsHeader(inf)


        list = []
        tables = data.sheets()
        titles = tables[0].row_values(0)#excel表头

        for t in tables:#遍历所有Sheet
            nrows = t.nrows
            for n in range(1, nrows):#遍历所有行
                app=self.getCellsValue(t.row_values(n),titles,tup)

                #self.getCellsValue1(t.row_values(n),titles,tup)

                if app:
                    list.append(app)
                    print app
        return list

    #取出行内符合条件的单元格内容
    def getCellsValue(self,row_values,titles,tup):
        desc = u'用例描述'


        cells={}
        if row_values:
            for i in range(len(titles)):#元组遍历
                #if not type(row[i]) is types.FloatType:
                if titles[i] in tup:
                    if titles[i] == desc:
                        cells[titles[i]] = self.getCellsValue1(row_values[i])
                    else:
                        cells[titles[i]] = row_values[i]
            return cells

    #取出行内符合条件的单元格内容
    def getCellsValue1(self,row_values,titles,tup):
        xls_header_keys=[]
        xls_header_vals=[]

        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        d=files.readConfigs(PATH('./config/settings.cfg'),'excel')

        for key,value in d.items():
            xls_header_keys.append(key)
            xls_header_vals.append(value)

        print self.getStrIndex(xls_header_vals,u'用例描述')

        desc = u'用例描述'
        cells={}
        if row_values:
            for i in range(len(titles)):
                #if not type(row[i]) is types.FloatType:

                if titles[i] in xls_header_vals:
                    if titles[i]==desc:
                        cells[titles[i]] = self.getInfValue(row_values[i])
                    else:
                        cells[titles[i]] = row_values[i]
            return cells

    def getStrIndex(self,lists,str):
        for i in range(0,len(lists)):
            if lists[i]==str:
                return i



    # def getInfValue(self,content):
    #     re_symbol = re.compile(r'(?<=\{\{).*?(?=}})')#接口正则
    #     re_url=re.compile(r'/[a-zA-z]+:\/\/[^\s]+/')
    #     match=re_symbol.search(content)
    #     m=re_url.search(content)
    #     if match:
    #         return match.group()
    #     else:
    #         return ''


    #取出包含在{{}}内的地址，并验证是否是网址
    def getInfValue(self,content):
        re_symbol = re.compile(r'(?<=\{\{).*?(?=}})')#接口正则
        re_url=re.compile(r'/[a-zA-z]+:\/\/[^\s]+/')
        match=re_symbol.search(content)

        if match:
            m=match.group()
            return m
            # is_url=re_url.search(m)
            # if is_url:
            #     return is_url.group()
            # else:
            #     return ''
            # TODO: 验证网址.
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

        # for num in range(1, nrows):
        #     for c in range(0,cols):
        #         print table.row_values(num)[c]
        #         app={}
        #         for i in range(len(array)):#元组遍历
        #             #print array[i]
        #             if table.row_values(num)[c]==array[i]:
        #                 app[array[i]]=table.row_values(num)[c]
        #         list.append(app)
        # return list
        #     print table.row_values(num)[3]
        #     if table.row_values(num)[3]=='':
        #         pass
        #     app = {}
        #     for i in range(len(array)):
        #         app[array[i]]=table.row_values(num)[i]
        #     list.append(app)
        # return list

            # for n in range(3,cols):
            #     print row[n]
        #return list

    # tables = excel.Excel(mPath + 'interface.xls').readByName(0, 'Sheet1')
    # for row in tables:
    #     print row











