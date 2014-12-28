# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        # QtCore.QAbstractTableModel.__init__(self, parent, *args)
        super(MyTableModel, self).__init__(parent, *args)
        self.arraydata = datain


    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0]['info'])

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self.arraydata[index.row()]['info'][index.column()])

