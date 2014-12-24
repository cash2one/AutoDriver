# coding=utf-8
__author__ = 'Administrator'

import os
import sys
import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from framework.gui.ui import index

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()

        self.ui = index.Ui_Form()
        self.ui.setupUi(self)
        self.ui.table_task.setHorizontalHeaderLabels(['姓名','身高','体重'])
