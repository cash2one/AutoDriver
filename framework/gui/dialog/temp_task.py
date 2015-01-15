# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.gui.views import temp_task_ui


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TaskExecDialog(QDialog, temp_task_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.chk_value = ()
        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 10))
        self.show_testcase()


    def show_testcase(self):
        case_path = PATH('../../../testcase/')

        for parent, dirnames, filenames in os.walk(case_path):
            if len(dirnames) == 0:
                f = parent[len(case_path) + 1:len(parent)]
                self.chk_value += (parent,)
                qc = QCheckBox()
                qc.setText(f)
                self.folderLayout.addWidget(qc)
