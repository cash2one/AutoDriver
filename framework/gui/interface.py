# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from framework.gui.ui import interface_ui


class InterfaceForm(QWidget, interface_ui.Ui_Form):
    def __init__(self):
        super(InterfaceForm, self).__init__()

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))

