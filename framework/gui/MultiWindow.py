# -*- coding: utf-8 -*-

import sys
import time
import threading

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from framework.gui.ui import main_window, ui_test2, ui_test3, index, login_ja
from framework.util import jira
from framework.core import the


class LoginDialog(QDialog):
    def __init__(self, ui):
        QDialog.__init__(self)
        self.ui = ui
        ui.setupUi(self)
        # self.isLogin = False
        self.connect(self.ui.btn_login, SIGNAL("clicked()"), self.login_action)
        self.connect(self.ui.btn_cancel, SIGNAL("clicked()"), self.confirm)
        self.connect(self, SIGNAL("loginFinish()"), self.confirm)
        self.connect(self, SIGNAL("loginError()"), self.time_out)

    def time_out(self):
        self.ui.lbl_info.setText(u'登录超时，账号密码错误.')

    def login_action(self):
        username = self.ui.txt_username.text()
        pwd = self.ui.txt_pwd.text()
        self.ui.btn_login.setText(u'登录中..')
        self.ui.btn_login.setEnabled(False)

        login = LoginFor405(self,username,pwd)
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
        #传递给全局的the.JIRA
        if the.JIRA==None:
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

            if self.timeout<=0:
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
        self.widget

        self.load_index()

    def loggg(self):
        self.initMainWinEvent()
        self.connect(self.action_JIRA, SIGNAL("clicked()"), self.login_dialog)

    # 打开第一个窗口
    def load_index(self):
        import index

        form=index.MainForm()
        form.setupUi(self.widget)

        #self.initMainWinEvent()  # 初始化主界面的事件
        #self.firstUi = index.Ui_Form()
        # w1 = QWidget(self.widget)
        # self.firstUi.setupUi(w1)

        #self.connect(self.firstUi.pushButton, SIGNAL("clicked()"), self.login_dialog)

    def testt(self):
        dialog = QDialog()
        r = dialog.exec_()  # 运行对话框
        if r:
            pass

    # 打开第二个窗口
    def btn2_click(self):
        self.initMainWinEvent()
        self.secondUi = ui_test2.Ui_Form()
        w2 = QWidget(self.widget)
        self.secondUi.setupUi(w2)

        project = 'IDRIVERC'
        start = '10'
        end = '20'
        if the.JIRA!=None:
            p = the.JIRA.get(
                '/rest/api/2/search?jql=project+%3D+' + project + '&startAt=' + start + '&maxResults=' + end)

            self.secondUi.label.setText(str(p['maxResults']))

    # 打开第三个窗口
    def btn3_click(self):
        self.initMainWinEvent()
        #将窗体定义成类成员变量
        self.thridUi = ui_test3.Ui_Form()
        w3 = QWidget(self.widget)
        self.thridUi.setupUi(w3)

    #通过单击第一个窗口里的按钮，弹出第四个窗口
    def login_dialog(self):
        login_j = login_ja.Ui_Form()
        login = LoginDialog(login_j)

        login.exec_()


    #初始化主界面，进行按钮的动态绑定
    def initMainWinEvent(self):
        self.setupUi(self)
        # if the.JIRA!=None:
        #     self.statusBar().showMessage(the.JIRA.dislayName)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.load_index)
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.btn2_click)
        self.connect(self.pushButton_3, SIGNAL("clicked()"), self.btn3_click)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
