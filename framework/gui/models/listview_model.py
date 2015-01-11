# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4 import QtCore


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


class TreeModel(QtCore.QAbstractListModel):
    def __init__(self, datain, parent=None):
        super(TreeModel, self).__init__(parent)
        self.listdata = datain
        self.rootItem = TreeItem((u'接口列表', u'描述'))


    # def data(self, index, role):
        # if index.isValid() and role == Qt.DisplayRole:
        # return QVariant(self.listdata[index.row()]['name'])
        # else:
        #     return QVariant()

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == QtCore.Qt.CheckStateRole:          #被选中项是checkbox
            if item.parent() == self.rootItem:        #如果是根的话，直接返回
                return None
            if item.childCount()>0:                   #如果是有子项的话，直接返回，这个可以根据需要调整。当需要成组选择的时候，必须保留
                return None
            if index.column()==0:
                for x in self.checkLisk:              #检查该项是否在checkList中，如果在将其设为选中状态
                    if x == index:
                        return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked

        if role != QtCore.Qt.DisplayRole:
            return None

        return item.data(index.column())

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.CheckStateRole and index.column()==0:
            if value == QtCore.Qt.Unchecked:
                self.checkLisk.remove(index)
                self.emit(QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"),
                          index, index)
            else:
                self.checkLisk.append(index)
                self.emit(QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"),
                          index, index)
            return True

    def flags(self, index):
        if not index.isValid() :
            return QtCore.Qt.NoItemFlags
        result = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        if index.column()==0:                          #只让第一列显示checkbox
            result |= QtCore.Qt.ItemIsUserCheckable
        return result


    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()


    def setupModelData1(self, lines, parent):
        pass

    def setupModelData(self, lines, parent):
        parents = [parent]
        indentations = [0]

        number = 0
        while number < len(lines):
            position = 0
            while position < len(lines[number]):
                if lines[number][position] != ' ':
                    break
                position += 1

            lineData = lines[number][position:].trimmed()

            if lineData:
                # Read the column data from the rest of the line.
                columnData = [s for s in lineData.split('\t') if s]

                if position > indentations[-1]:
                    # The last child of the current parent is now the new
                    # parent unless the current parent has no children.

                    if parents[-1].childCount() > 0:
                        parents.append(parents[-1].child(parents[-1].childCount() - 1))
                        indentations.append(position)

                else:
                    while position < indentations[-1] and len(parents) > 0:
                        parents.pop()
                        indentations.pop()

                # Append a new item to the current parent's list of children.
                parents[-1].appendChild(TreeItem(columnData, parents[-1]))

            number += 1