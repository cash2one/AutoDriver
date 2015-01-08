# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from framework.gui.ui import monitor_ui


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MonitorDialog(QDialog, monitor_ui.Ui_Dialog):
    def __init__(self):
        super(MonitorDialog, self).__init__()

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
