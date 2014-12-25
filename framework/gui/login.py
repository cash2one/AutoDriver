# -*- coding: utf-8 -*-

import threading
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import login_ja
from framework.core import the, jira


class MainDialog(QDialog, login_ja.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)

        # self.ui = login_ja.Ui_Form()
        #self.ui.setupUi(self)
        self.setupUi(self)

        self.connect(self.btn_login, SIGNAL("clicked()"), self.login_action)
        self.connect(self.btn_cancel, SIGNAL("clicked()"), self.confirm)
        self.connect(self, SIGNAL("loginFinish()"), self.confirm)
        self.connect(self, SIGNAL("loginError()"), self.time_out)

    def time_out(self):
        self.ui.lbl_info.setText(u'登录超时，账号密码错误.')

    def login_action(self):
        username = self.txt_username.text()
        pwd = self.txt_pwd.text()
        self.btn_login.setText(u'登录中..')
        self.btn_login.setEnabled(False)

        login = LoginFor405(self, username, pwd)
        login.start()

    def confirm(self):
        # self.ui.lineEditValidateNum.setText("XXXXXX")   #测试给弹出的对话框里的元素赋值
        self.reject()  # 关闭窗口


class LoginFor405(threading.Thread):
    '''
    JIRA405错误的解决方案
    '''

    def __init__(self, ui, u_name, u_pwd):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.startLogin = False
        self.ui = ui
        self.timeout = 20
        # 传递给全局的the.JIRA
        if the.JIRA == None:
            the.JIRA = jira.JIRA(u_name, u_pwd)

    def run(self):
        while not self.thread_stop:
            if not the.JIRA.isActive:
                self.start_login()
            else:
                print 'login success!'
                # emit 方法用来发射信号
                self.ui.emit(SIGNAL("loginFinish()"))
                self.stop()
            time.sleep(1)

            if self.timeout <= 0:
                self.ui.emit(SIGNAL("loginError()"))
                self.stop()

    def start_login(self):
        if self.startLogin:
            the.JIRA.userActive()
            self.timeout -= 1
        else:
            the.JIRA.login()
            self.startLogin = True

    def stop(self):
        self.thread_stop = True