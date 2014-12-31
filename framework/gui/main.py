# -*- coding: utf-8 -*-

import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import main_ui
from framework.core import the
import home, dialog, jiras,base


class MainWindow(QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.frm_home = None
        self.frm_jira = None
        self.dlg_login = None
        self.dlg_select_task = None
        self.dlg_new_task = None
        self.dlg_task = None

        self.connect(self.menu_login, SIGNAL("triggered()"), self.login_dialog)
        # self.connect(self.menu_login, SIGNAL(("triggered()")), self.login_dialog)
        self.connect(self.toolbar_home, SIGNAL(("triggered()")), self.load_index)
        self.connect(self.toolbar_jira, SIGNAL("triggered()"), self.load_jira_main)
        self.connect(self, SIGNAL("startLogin()"), self.login_dialog)



        # 显示托盘信息
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("./ui/res/wp.ico"))
        self.trayIcon.show()
        self.connect(self.trayIcon, SIGNAL("activated()"), self.trayClick)
        # self.trayIcon.activated.connect(self.trayClick) #点击托盘
        self.trayMenu()  # 右键菜单

        self.setFont(QFont("Microsoft YaHei", 9))
        self.showMaximized()


        self.load_index()

    def not_login(self):
        print 'not loginsssss'

    def save_task(self,arg):
        self.task_data+=arg
        print self.task_data

    def update_user(self):
        usrname = the.JIRA.userName.capitalize()
        self.toolbar_jira.setText(usrname)

    def test(self):
        print 'gwegwe'

    def trayMenu(self):
        # 右击托盘弹出的菜单
        img_main = QIcon("./ui/res/app.png")
        img_exit = QIcon("./ui/res/exit.png")
        self.trayIcon.setToolTip(u'Woodpecker')
        self.restoreAction = QAction(img_main, u"打开主窗口", self)
        self.restoreAction.triggered.connect(self.showNormal)
        self.quitAction = QAction(img_exit, u"退出", self)
        self.quitAction.triggered.connect(qApp.quit)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu)

    def load_index(self):
        self.frm_home = home.HomeForm()
        self.frm_home.connect(self.frm_home, SIGNAL("notLogin"), self.login_dialog)
        self.setCentralWidget(self.frm_home)

    def outSelect(self, Item=None):
        if Item == None:
            return
        print(unicode(Item))

    def trayClick(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showNormal()
        else:
            pass

    def load_jira_main(self):
        if the.JIRA == None:
            self.msgHandler()
            return

        if the.JIRA.isActive:
            self.frm_jira = jiras.JIRAForm()
            self.setCentralWidget(self.frm_jira)
        else:
            self.msgHandler()


    def msgHandler(self):
        ret = QMessageBox.warning(self, u'未登录',
                                  u"\n你还没有登录JIRA，点击确定登录  \n",
                                  QMessageBox.Save | QMessageBox.Cancel)
        if ret == QMessageBox.Save:
            self.emit(SIGNAL("startLogin()"))
        elif ret == QMessageBox.Cancel:
            pass

    def login_dialog(self):
        if the.JIRA != None:
            if the.JIRA.isActive:
                return

        if self.dlg_login == None:
            self.dlg_login = jiras.LoginDialog()
            self.connect(self.dlg_login, SIGNAL("loginFinish"), self.update_user)
        self.dlg_login.exec_()


    def show_msg(self, txt):
        msg = dialog.MsgDialog(txt)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
