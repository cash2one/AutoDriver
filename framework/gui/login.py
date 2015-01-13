# coding=utf-8
__author__ = 'guguohai@outlook.com'

import json

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtNetwork

from framework.gui.views import login_ui
from framework.core import the


ja = the.jira

class LoginDialog(QDialog, login_ui.Ui_Form):
    def __init__(self):
        super(LoginDialog, self).__init__()
        # QDialog.__init__(self)

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 10))
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框

        self.txt_username.setFocus()
        self.txt_pwd.setEchoMode(QLineEdit.Password)  # 将其设置为密码框
        self.btn_login.setStyleSheet(
            "border:0;background-image:url(./views/res/login_btn_normal.png);background-repeat:no-repeat;padding:0;margin:0")
        self.btn_cancel.setStyleSheet(
            "border:0;background-image:url(./views/res/login_btn_normal.png);background-repeat:no-repeat;padding:0;margin:0")

        self.connect(self.btn_login, SIGNAL("clicked()"), self.login_action)
        self.connect(self.btn_cancel, SIGNAL("clicked()"), self.confirm)
        # self.connect(self, SIGNAL("loginFinish"), self.confirm)
        # self.connect(self, SIGNAL("loginError"), self.time_out)
        self.setBackgroundImg()
        self.user_name = ''
        # self.net_manager = net.NetManager(jira.cookie, self)


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
        png.load("./views/res/login.png")
        palette1 = QPalette(self)
        palette1.setBrush(self.backgroundRole(), QBrush(png))
        self.widget.setPalette(palette1)

    def time_out(self):
        self.btn_login.setText(u'登录')
        self.btn_login.setEnabled(True)
        self.lbl_info.setText(u'登录超时，账号密码错误.')

    def net_access(self, api, reply_func):
        m1 = QtNetwork.QNetworkAccessManager(self)
        m1.setCookieJar(ja.cookie)
        m1.finished.connect(reply_func)
        req1 = QtNetwork.QNetworkRequest(QUrl(api))
        m1.get(req1)


    def login_action(self):
        self.user_name = self.txt_username.text()
        pwd = self.txt_pwd.text()

        if QString(self.user_name).isEmpty() or QString(pwd).isEmpty():
            self.lbl_info.setText(u'账号密码不能为空！')
            return

        api = '/rest/gadget/1.0/login?os_username=%s&os_password=%s&os_captcha=' % (self.user_name, pwd)

        # nm = net.NetManager()
        # nm.get(self,jira.cookie, api, self.on_reply)
        # self.net_manager.get(jira.host + api, self.on_reply)
        self.net_access(ja.host + api, self.on_reply)

        self.btn_login.setText(u'登录中..')
        self.btn_login.setEnabled(False)

    def confirm(self):
        # self.ui.lineEditValidateNum.setText("XXXXXX")   #测试给弹出的对话框里的元素赋值
        self.btn_login.setText(u'登录')
        self.btn_login.setEnabled(True)
        self.reject()  # 关闭窗口

    def on_reply(self, reply):
        if reply.error() != reply.NoError:
            api = '/rest/api/2/user?username=%s' % self.user_name

            # self.net_manager.get(jira.host + api, self.on_user_reply)
            self.net_access(ja.host + api, self.on_user_reply)
            print reply.error()


    def on_user_reply(self, reply):
        if reply.error() == reply.NoError:
            # con = QString(reply.readAll())
            # print reply.rawHeaderList()
            # con = unicode(QString(reply.readAll()))
            con = str(QString(reply.readAll()).toLatin1())

            try:
                dicts = json.loads(con)
                ja.userName = dicts['name']
                ja.isActive = True
                self.emit(SIGNAL("loginFinish"), ja.userName)

                self.confirm()
            except ValueError:
                pass
        else:
            ja.isActive = False
            self.time_out()
            # self.emit(SIGNAL("loginError"))
            print reply.error()
            print reply.errorString()

            return


# class LoginFor405(threading.Thread):
# '''
# JIRA405错误的解决方案
# '''
#
# def __init__(self, ui, u_name, u_pwd):
# threading.Thread.__init__(self)
# self.thread_stop = False
# self.isStartLogin = False
# self.ui = ui
# self.timeout = 15
#         self.u_name = u_name
#         self.u_pwd = u_pwd
#
#     def run(self):
#         while not self.thread_stop:
#             if not base.third.isActive:
#                 if not self.isStartLogin:
#                     base.third.login(self.u_name, self.u_pwd)
#                     self.isStartLogin = True
#                 else:
#                     base.third.userActive(self.u_name)
#                     self.timeout -= 1
#             else:
#                 print 'login success!'
#                 # emit 方法用来发射信号
#                 self.ui.emit(SIGNAL("loginFinish"))
#                 self.stop()
#             time.sleep(1)
#
#             if self.timeout <= 0:
#                 self.ui.emit(SIGNAL("loginError"))
#                 self.stop()
#
#     def stop(self):
#         self.thread_stop = True

