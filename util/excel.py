# coding=utf-8
__author__ = 'guohai@live.com'

import xlrd


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
    def readByIndex(self, column_index, by_index):
        data = self.openExcel()
        table = data.sheets()[by_index]
        nrows = table.nrows  # 行数
        #cols = table.ncols  # 列数
        col_names = table.row_values(column_index)  # 某一行数据
        list = []
        for num in range(1, nrows):
            row = table.row_values(num)
            if row:
                app = {}
                for i in range(len(col_names)):
                    app[col_names[i]] = row[i]
                list.append(app)
        return list



    # tables = excel.Excel(mPath + 'interface.xls').readByName(0, 'Sheet1')
    # for row in tables:
    #     print row











