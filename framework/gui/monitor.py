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
        self.btn_end.hide()

        self.btn_start.clicked.connect(self.start_monitor)
        self.btn_end.clicked.connect(self.end_monitor)

    def start_monitor(self):
        self.btn_start.hide()
        self.btn_end.show()

    def end_monitor(self):
        self.file_dialog()

    def file_dialog(self):
        fd = QFileDialog(self)
        self.filename = fd.getSaveFileName()
        fobj = open(self.filename, 'w')
        fobj.write(self.txt_msg.toPlainText())
        fobj.close()
        self.txt_msg.setText('File saved!!')
        # fd.getOpenFileName()
        # from os.path import isfile
        #
        # if isfile(self.filename):
        # s = open(self.filename, 'r').read()