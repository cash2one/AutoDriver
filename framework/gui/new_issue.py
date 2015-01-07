# coding=utf-8
__author__ = 'guguohai@outlook.com'

import json
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import new_issue_ui
from framework.util import convert
from framework.gui.base import *


class IssueDialog(QDialog, new_issue_ui.Ui_Dialog):
    def __init__(self, data=None):
        QDialog.__init__(self)

        self.data = data

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
