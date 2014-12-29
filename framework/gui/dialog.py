# -*- coding: utf-8 -*-

import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import login_ui, msg_ui, autos_ui, task_ui
from framework.core import the, jira
from framework.gui.models import tree_model


class LoginDialog(QDialog, login_ui.Ui_Form):
    def __init__(self):
        super(LoginDialog, self).__init__()
        # QDialog.__init__(self)

        # self.ui = login_ja.Ui_Form()
        # self.ui.setupUi(self)
        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 10))
        self.setWindowFlags(Qt.FramelessWindowHint)  #无边框
        self.connect(self.btn_login, SIGNAL("clicked()"), self.login_action)
        self.connect(self.btn_cancel, SIGNAL("clicked()"), self.confirm)
        self.connect(self, SIGNAL("loginFinish()"), self.confirm)
        self.connect(self, SIGNAL("loginError()"), self.time_out)
        self.setBackgroundImg()


    def mousePressEvent(self, event):
        # 定义鼠标点击事件
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event):
        # 定义鼠标移动事件
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


    def setBackgroundImg(self):
        png = QPixmap(self)
        png.load("./ui/res/login.png")
        palette1 = QPalette(self)
        palette1.setBrush(self.backgroundRole(), QBrush(png))
        self.widget.setPalette(palette1)


        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(15)
        # self.shadow.setOffset(5,5)
        # self.widget.setGraphicsEffect(self.shadow)

    def time_out(self):
        self.lbl_info.setText(u'登录超时，账号密码错误.')

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
        # self.startLogin = False
        self.useActive = 0
        self.ui = ui
        self.timeout = 15
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
                print 'thread finish:',the.JIRA.dislayName
                self.stop()
            time.sleep(1)

            if self.timeout <= 0:
                self.ui.emit(SIGNAL("loginError()"))
                self.stop()

    def start_login(self):
        # if self.startLogin:
        the.JIRA.userActive()
        self.useActive += 1
        self.timeout -= 1

        # 如果2次以后，还没有获取到用户Active，就使用登录
        if self.useActive == 2:
            the.JIRA.login()
            print 'not active,use login'
            # self.startLogin = True

    def stop(self):
        self.thread_stop = True


class MsgDialog(QDialog, msg_ui.Ui_Dialog):
    def __init__(self, msg_txt):
        super(MsgDialog, self).__init__()

        self.setupUi(self)

        self.lbl_msg.setText(msg_txt)


class SelectScriptsDialog(QDialog, autos_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)

        # self.ui = select_task.Ui_Form()
        # self.ui.setupUi(self)
        self.setupUi(self)

        f = QFile(':/default.txt')
        f.open(QIODevice.ReadOnly)
        model = tree_model.TreeModel(f.readAll())
        f.close()
        self.treeView.setModel(model)


    def confirm(self):
        self.reject()  # 关闭窗口


class TaskDialog(QDialog, task_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)

        detailLayout = QGridLayout(self.widget_task)
        taskv = QTableView()
        detailLayout.addWidget(taskv, 0, 1)
        self.widget_task.hide()

        self.hzLayout.setSizeConstraint(QLayout.SetFixedSize)

        # self.btn_Automate.hide()
        # self.connect(self.btn_Automate, SIGNAL("clicked()"), self.select_tasks)
        self.connect(self, SIGNAL("selectTask()"), self.select_tasks)
        self.connect(self.cmb_TaskType, SIGNAL('activated(QString)'), self.onActivated)

    def onActivated(self, txt):
        if txt == u'自动化':
            # self.btn_Automate.show()
            self.widget_task.show()
            # self.emit(SIGNAL("selectTask()"))
        else:
            self.widget_task.hide()

            # self.label.setText(txt)
            # self.label.adjustSize()

    def confirm(self):
        self.reject()  # 关闭窗口

    def select_tasks(self):
        t = SelectScriptsDialog()
        t.exec_()
