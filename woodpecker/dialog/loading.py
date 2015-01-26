# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os

from PyQt4.QtGui import *
from PyQt4 import QtCore

from woodpecker.views import loading_ui


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoadingDialog(QDialog, loading_ui.Ui_Dialog):
    def __init__(self):
        super(LoadingDialog, self).__init__()

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
