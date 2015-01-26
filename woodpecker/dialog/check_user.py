# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from woodpecker.views import user_ui


class UserDialog(QDialog, user_ui.Ui_Dialog):
    def __init__(self):
        super(UserDialog, self).__init__()

        self.setupUi(self)

        self.model = QStandardItemModel()
        self.model.itemChanged.connect(self.on_item_changed)
        # view = QDeclarativeView()
        # view.setSource(QUrl("./views/user.qml"))
        # view.show()
        for a in range(0, 5):
            item = QStandardItem("Item-" + str(a))
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(QVariant(Qt.Checked), Qt.CheckStateRole)
            self.model.appendRow(self.item)
        self.lv_user.setModel(self.model)

        # 连接信号和槽
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def getUser(self):
        print self.lv_user.item
        aa = []
        for a in self.lv_user.selectedIndexes():
            aa.append(a)