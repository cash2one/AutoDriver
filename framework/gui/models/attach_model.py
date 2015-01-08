# coding=utf-8
__author__ = 'guguohai@outlook.com'

import sys
import os
from PyQt4 import QtGui, QtCore


class MyListModel(QtCore.QAbstractListModel):
    def __init__(self, datain, parent=None, *args):
        QtCore.QAbstractListModel.__init__(self, parent, *args)
        self.listdata = datain

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.listdata)

    def data(self, index, role):
        if index.isValid() and role == QtCore.Qt.DecorationRole:
            s = QtCore.QSize(250, 200)
            print self.listdata[index.row()]
            pix = QtGui.QPixmap(self.listdata[index.row()])
            pix.scaled(s, QtCore.Qt.KeepAspectRatio)
            return QtGui.QIcon(pix)
            #return QtGui.QIcon(QtGui.QPixmap(self.listdata[index.row()]).scaled(s, QtCore.Qt.KeepAspectRatio))
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(os.path.splitext(os.path.split(self.listdata[index.row()])[-1])[0])
        else:
            return QtCore.QVariant()


        # model = QStandardItemModel()
        # item = QStandardItem("Item")
        # item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        # item.setData(QVariant(Qt.Checked), Qt.CheckStateRole)
        # model.appendRow(item)
        # self.lv_user.setModel(model)