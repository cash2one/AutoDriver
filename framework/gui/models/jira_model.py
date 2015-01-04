# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, header, datain, parent=None, *args):
        # QtCore.QAbstractTableModel.__init__(self, parent, *args)
        super(MyTableModel, self).__init__(parent, *args)
        self.arraydata = datain
        self.header = header


    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        return QtCore.QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.header[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

