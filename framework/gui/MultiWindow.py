# -*- coding: utf-8 -*-

import sys
import time
import threading

from PyQt4 import QtGui, QtCore,QtNetwork
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from framework.gui.ui import main_window, ui_test2, ui_test3, ui_test1, login_jira
from framework.util import jira
from framework.core import the



class LoginDialog(QtGui.QDialog):
    def __init__(self, ui):
        QtGui.QDialog.__init__(self)
        self.ui = ui
        ui.setupUi(self)
        self.isLogin = False
        self.connect(self.ui.btnLogin, QtCore.SIGNAL("clicked()"), self.login_action)
        self.connect(self.ui.btnCancel, QtCore.SIGNAL("clicked()"), self.confirm)

    def login_action(self):
        username = self.ui.txt_username.text()
        pwd = self.ui.txt_pwd.text()
        the.account = jira.JIRA()
        self.isLogin = the.account.login(username, pwd)
        aa=self.CheckLogin(self)
        aa.start()

    def confirm(self):
        # self.ui.lineEditValidateNum.setText("XXXXXX")   #测试给弹出的对话框里的元素赋值
        self.reject()  #关闭窗口


    class CheckLogin(threading.Thread):
        def __init__(self, ui):  # ,db_path):
            threading.Thread.__init__(self)
            self.thread_stop = False
            #self.isLogin=isLogin
            self.ui=ui


        def run(self):
            while not self.thread_stop:
                if self.isLogin:
                    self.ui.reject()
                    self.stop()

            time.sleep(5)

        def stop(self):
            self.thread_stop = True


class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    """
    Class documentation goes here.
    """
    firstUi = None
    secondUi = None
    thridUi = None

    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.connect(self.action_save, SIGNAL("clicked()"), self.testt)
        self.btn1_click()

    # 打开第一个窗口
    def btn1_click(self):
        self.initMainWinEvent()  #初始化主界面的事件
        self.firstUi = ui_test1.Ui_Form()
        w1 = QWidget(self.widget)
        self.firstUi.setupUi(w1)

        self.connect(self.firstUi.pushButton, SIGNAL("clicked()"), self.login_dialog)

    def testt(self):
        dialog = QDialog()
        r = dialog.exec_()  # 运行对话框
        if r:
            pass

    #打开第二个窗口
    def btn2_click(self):
        self.initMainWinEvent()
        self.secondUi = ui_test2.Ui_Form()
        w2 = QWidget(self.widget)
        self.secondUi.setupUi(w2)

        project = 'IDRIVERC'
        start = '10'
        end = '20'
        p = the.account.get(
            '/rest/api/2/search?jql=project+%3D+' + project + '&startAt=' + start + '&maxResults=' + end)

        self.secondUi.label.setText(str(p['maxResults']))

    #打开第三个窗口
    def btn3_click(self):
        self.initMainWinEvent()
        #将窗体定义成类成员变量
        self.thridUi = ui_test3.Ui_Form()
        w3 = QWidget(self.widget)
        self.thridUi.setupUi(w3)

    #通过单击第一个窗口里的按钮，弹出第四个窗口
    def login_dialog(self):
        login_ja = login_jira.Ui_Form()
        login = LoginDialog(login_ja)
        login.exec_()


    #初始化主界面，进行按钮的动态绑定
    def initMainWinEvent(self):
        self.setupUi(self)

        self.connect(self.pushButton, SIGNAL("clicked()"), self.btn1_click)
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.btn2_click)
        self.connect(self.pushButton_3, SIGNAL("clicked()"), self.btn3_click)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
