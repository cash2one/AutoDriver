# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtNetwork
from framework.gui.ui import testcase_ui


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestCaseForm(QWidget, testcase_ui.Ui_Form):
    def __init__(self):
        super(TestCaseForm, self).__init__()

        self.setupUi(self)

        self.http = QtNetwork.QHttp(parent=self)
        # 绑定 done 信号
        self.http.done.connect(self.on_req_done)
        self.url = QUrl("http://www.weather.com.cn/data/sk/101190101.html")

        # 设置主机
        self.http.setHost(self.url.host(), self.url.port(80))
        self.getId = self.http.get(self.url.path())

    def on_req_done(self, error):
        if not error:
            print "Success"
            con = self.http.readAll()
            self.textEdit.setPlainText(QString(con))
        else:
            print "Error"