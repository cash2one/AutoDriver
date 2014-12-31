# -*- coding: utf-8 -*-

import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import login_ui, msg_ui, autos_ui, task_ui
from framework.core import the
from framework.gui.models import tree_model


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


class TaskDialog(QDialog, task_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)

        detailLayout = QGridLayout(self.widget_task)
        taskv = QTableView()
        detailLayout.addWidget(taskv, 0, 1)
        self.widget_task.hide()

        self.hzLayout.setSizeConstraint(QLayout.SetFixedSize)

        # self.btn_Automate.hide()
        # self.connect(self.btn_Automate, SIGNAL("clicked()"), self.select_tasks)
        self.connect(self, SIGNAL("selectTask()"), self.select_tasks)
        self.connect(self.cmb_TaskType, SIGNAL('activated(QString)'), self.onActivated)

    def onActivated(self, txt):
        if txt == u'自动化':
            # self.btn_Automate.show()
            self.widget_task.show()
            # self.emit(SIGNAL("selectTask()"))
        else:
            self.widget_task.hide()

            # self.label.setText(txt)
            # self.label.adjustSize()

    def confirm(self):
        self.reject()  # 关闭窗口

    def select_tasks(self):
        t = SelectScriptsDialog()
        t.exec_()
