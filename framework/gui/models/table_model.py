# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, header, datain, parent=None, *args):
        # QtCore.QAbstractTableModel.__init__(self, parent, *args)
        super(MyTableModel, self).__init__(parent, *args)
        self.arraydata = datain
        self.header = header  # (u'编号', u'任务名称', u'任务状态', u'任务类型', u'优先级', u'执行人', u'创建人', u'创建时间')

    def update(self, dataIn):
        self.arraydata = dataIn

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])  # ['info'])

    def rowContent(self, index):
        return self.arraydata[index]  # ['info']

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()

        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        else:
            i = index.row()
            j = index.column()
            return QtCore.QVariant(self.arraydata[i][j])  # [index.row()]['info'][index.column()])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.header[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

        # #返回表头名称,(行号或列号，水平或垂直，角色)
        # def headerData(self,index,orientation,role):
        # if role != QtCore.Qt.DisplayRole:
        #         return QtCore.QVariant()
        #
        #     #self.tt = (u'编号', u'任务名称', u'任务状态', u'任务类型', u'优先级', u'执行人', u'创建人', u'创建时间')
        #     return self.arraydata[index]#['info']
        #
        # def flags(self, index):
        #     return QtCore.Qt.ItemIsEnabled

