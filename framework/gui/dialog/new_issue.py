# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.views import new_issue_ui,label_btn


class IssueDialog(QDialog, new_issue_ui.Ui_Dialog):
    def __init__(self, data=None):
        QDialog.__init__(self)

        self.data = data

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))

        lbl = label_btn.LabelButton()
        lbl.setText(u'自定义控件')
        self.hz_layout.addWidget(lbl)

        self.connect(lbl, SIGNAL("clicked()"), self.print_dd)

        # lists = [{'k1': 'aaaa', 'k2': 'bbbb'}, {'k1': 'cccc', 'k2': 'ggggg'}]
        #
        # for att in lists:
        # btn = QPushButton(att['k1'])
        #     self.connect(btn, SIGNAL("clicked()"), lambda arg=att['k2']: self.open_file_browser(arg))
        #     self.hz_layout.addWidget(btn)

    def print_dd(self):
        print 'new_issue...'

    def open_file_browser(self, con):
        print con
        # fileBrowser = file_browser.FileDialog(con, self.net_access)
        # fileBrowser.setFixedSize(600, 500)
        # fileBrowser.exec_()