# -*- coding: utf-8 -*-

import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import msg_ui, autos_ui, user_ui
from framework.gui.models import tree_model, userlist_model
from PyQt4.QtDeclarative import QDeclarativeView

class UserDialog(QDialog, user_ui.Ui_Dialog):
    def __init__(self):
        super(UserDialog, self).__init__()

        self.setupUi(self)

        model = QStandardItemModel()

        # view = QDeclarativeView()
        # view.setSource(QUrl("./ui/user.qml"))
        # view.show()
        for a in range(0, 5):
            item = QStandardItem("Item-" + str(a))
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(QVariant(Qt.Checked), Qt.CheckStateRole)
            model.appendRow(item)
        self.lv_user.setModel(model)

        # self.lv_user.setViewMode(QListView.IconMode)
        # crntDir = "./ui/res"
        # # create table
        # list_data = []
        # philes = os.listdir(crntDir)
        # for phile in philes:
        #     if phile.endswith(".png"):
        #         list_data.append(os.path.join(crntDir, phile))
        # lm = userlist_model.MyListModel(list_data, self)
        # self.lv_user.setModel(lm)


class MsgDialog(QDialog, msg_ui.Ui_Dialog):
    def __init__(self, msg_txt):
        super(MsgDialog, self).__init__()

        self.setupUi(self)
        self.lbl_msg.setText(msg_txt)


class SelectScriptsDialog(QDialog, autos_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)

        # self.ui = select_task.Ui_Form()
        # self.ui.setupUi(self)
        self.setupUi(self)

        f = QFile(':/default.txt')
        f.open(QIODevice.ReadOnly)
        model = tree_model.TreeModel(f.readAll())
        f.close()
        self.treeView.setModel(model)


    def confirm(self):
        self.reject()  # 关闭窗口


# class TaskDialog(QDialog, task_ui.Ui_Form):
#     def __init__(self):
#         QDialog.__init__(self)
#
#         self.setupUi(self)
#
#         self.connect(self, SIGNAL("selectTask()"), self.select_tasks)
#         self.connect(self.cmb_TaskType, SIGNAL('activated(QString)'), self.onActivated)
#
#     def onActivated(self, txt):
#         if txt == u'自动化':
#             # self.btn_Automate.show()
#             self.widget_task.show()
#             # self.emit(SIGNAL("selectTask()"))
#         else:
#             self.widget_task.hide()
#
#             # self.label.setText(txt)
#             # self.label.adjustSize()
#
#     def confirm(self):
#         self.reject()  # 关闭窗口
#
#     def select_tasks(self):
#         t = SelectScriptsDialog()
#         t.exec_()
