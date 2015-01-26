# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4 import QtGui, QtCore


class QTableModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        # QtCore.QAbstractTableModel.__init__(self, parent, *args)
        super(QTableModel, self).__init__(parent, *args)
        self.arraydata = datain
        self.header = (u'脚本名', u'状态', u'结果')

    def updateAll(self, dataIn):
        self.arraydata = dataIn

    def updateRow(self, data, index):
        self.arraydata[index] = data


    def insertRows(self, data):
        self.arraydata += (data,)
        # self.beginInsertRows(QtCore.QModelIndex(), len(self.arraydata), len(self.arraydata))

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0:
            return len(self.arraydata[0])

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

            return QtCore.QVariant(self.arraydata[i][j])  # [index.row()]['info'][index.column()])

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
        # return self.arraydata[index]#['info']
        #
        # def flags(self, index):
        # return QtCore.Qt.ItemIsEnabled

