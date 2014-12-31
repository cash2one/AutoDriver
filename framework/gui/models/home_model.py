# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, header, datain, parent=None, *args):
        # QtCore.QAbstractTableModel.__init__(self, parent, *args)
        super(MyTableModel, self).__init__(parent, *args)
        self.arraydata = datain
        self.header = header
        # self.aa = (u'编号', u'任务名称', u'任务状态', u'任务类型', u'优先级', u'执行人', u'创建人', u'创建时间', '更新时间', u'执行时间', u'结束时间')

    def updateAll(self, dataIn):
        self.arraydata = dataIn

    def updateRow(self, data, index):
        self.arraydata[index]['row'] = data



    def insertRows(self,data):
        self.arraydata += (data,)
        #self.beginInsertRows(QtCore.QModelIndex(), len(self.arraydata), len(self.arraydata))

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0]['row'])

    def rowContent(self, index):
        return self.arraydata[index]

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()

        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        else:
            i = index.row()
            j = index.column()
            return QtCore.QVariant(self.arraydata[i]['row'][j])  # [index.row()]['info'][index.column()])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.header[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

        # #返回表头名称,(行号或列号，水平或垂直，角色)
        # def headerData(self,index,orientation,role):
        # if role != QtCore.Qt.DisplayRole:
        # return QtCore.QVariant()
        #
        # #self.tt = (u'编号', u'任务名称', u'任务状态', u'任务类型', u'优先级', u'执行人', u'创建人', u'创建时间')
        #     return self.arraydata[index]#['info']
        #
        # def flags(self, index):
        #     return QtCore.Qt.ItemIsEnabled

