# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4.QtCore import *


class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return len(self.itemData)

    def data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0


class TreeModel(QAbstractListModel):
    def __init__(self, datain, parent=None):
        super(TreeModel, self).__init__(parent)
        self.listdata = datain
        self.rootItem = TreeItem((u'接口列表', u'描述'))

    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)

    def data(self, index, role):
        # if index.isValid() and role == Qt.DisplayRole:
        #     return QVariant(self.listdata[index.row()]['name'])
        # else:
        #     return QVariant()
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == Qt.CheckStateRole:          #被选中项是checkbox
            if item.parent() == self.rootItem: #如果是根的话，直接返回
                return None
            if item.childCount()>0:  #如果是有子项的话，直接返回，这个可以根据需要调整。当需要成组选择的时候，必须保留
                return None
            if index.column()==0:
                for x in self.checkLisk:  #检查该项是否在checkList中，如果在将其设为选中状态
                    if x == index:
                        return Qt.Checked
                else:
                    return Qt.Unchecked

        if role != Qt.DisplayRole:
            return None

        return item.data(index.column())

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)
        return None