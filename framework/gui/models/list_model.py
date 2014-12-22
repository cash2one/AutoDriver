# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore


class MyListModel(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None):
        super(MyListModel, self).__init__(parent)
        self._data = data


    def rowCount(self, parent=QtCore.QModelIndex()):
        """
        这个方法返回了数据的行数
        也就是有多少个条目得数据
        """
        return len(self._data)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """
        根据当前index索引，返回当前的数据
        然后再由Qt进行渲染显示
        """

        # 如果当前得索引是不活动得
        if not index.isValid() or not 0 <= index.row() < self.rowCount():
            # 亦或者当前的索引值不在合理范围，即小于等于0，超出总行数
            return QtCore.QVariant()  # 返回一个QVariant，相当与空条目

        # 从索引取得当前的航号
        row = index.row()

        # 如果当前角色是DisplayRole
        if role == QtCore.Qt.DisplayRole:
            # 返回当前行的数据
            return self._data[row]

        # 如果角色不满足需求，则返回QVariant
        return QtCore.QVariant()

#
# def main():
#     app = QtGui.QApplication(sys.argv)
#
#     # 新建一个ListView
#     view = QtGui.QListView()
#     # 新建一个自定义Model
#
#     _data = [70, 90, 20, 50]
#     model = MyListModel(_data)
#     # 设置view的model
#     view.setModel(model)
#     view.show()
#
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()