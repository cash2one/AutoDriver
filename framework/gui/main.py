# -*- coding: utf-8 -*-

import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import main_ui
from framework.core import the
import home, dialog, jira
from framework.gui.models import jira_model


class MainWindow(QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # self.widget

        self.frm_home = None
        self.frm_jira = None
        self.dlg_login = None
        self.dlg_select_task = None
        self.dlg_new_task = None
        self.dlg_task = None
        self.tasks = None

        self.connect(self.menu_login, SIGNAL("triggered()"), self.login_dialog)
        # self.connect(self.menu_login, SIGNAL(("triggered()")), self.login_dialog)
        self.connect(self.toolbar_home, SIGNAL(("triggered()")), self.load_index)
        self.connect(self.toolbar_jira, SIGNAL("triggered()"), self.load_jira)
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
        self.frm_home.connect(self.frm_home.pushButton, SIGNAL("clicked()"), self.new_task)

        # self.frm_home.connect(self.frm_home.tv_task, SIGNAL("doubleClicked(const QModelIndex&)"),self.ddd)

        #self.frm_home.tv_task.rowDoubleClicked().connect(self.ddd)
        # self.connect(self.frm_home.table_task, SIGNAL("itemDoubleClicked(QTableWidgetItem*)"), self.outSelect)
        # self.self.frm_home.table_task.cellChanged.connect(self.makeDirty)
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

    def load_jira(self):
        if the.JIRA == None:
            self.msgHandler()
            return

        if the.JIRA.isActive:
            self.frm_jira = jira.JIRAForm()
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


    # 通过单击第一个窗口里的按钮，弹出第四个窗口
    def login_dialog(self):
        if the.JIRA != None:
            if the.JIRA.isActive:
                return

        if self.dlg_login == None:
            self.dlg_login = jira.LoginDialog()
            self.connect(self.dlg_login, SIGNAL("loginFinish"), self.update_user)
        self.dlg_login.exec_()


    def show_msg(self, txt):
        msg = dialog.MsgDialog(txt)
        msg.exec_()


    def new_task(self):
        if self.dlg_new_task == None:
            self.dlg_new_task = dialog.TaskDialog()
        self.dlg_new_task.exec_()

    # def show_current_task(self):
    #     current_row = self.frm_home.table_task.currentRow()
    #     row_data = self.tasks[current_row]['info']
    #     if self.dlg_task == None:
    #         self.dlg_task = dialog.TaskDialog()
    #
    #     self.dlg_task.txt_TaskName.setText(row_data[1])
    #     self.dlg_task.txt_Creator.setText(row_data[5])
    #     self.dlg_task.exec_()


class LoadNetData(threading.Thread):
    def __init__(self, ui, sign_value, url):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.ui = ui
        self.url = url
        self.sign_value = sign_value
        self.result = None
        self.isStart = False

    def run(self):
        while not self.thread_stop:
            print 'thread:::', self.url
            if not self.isStart:
                self.result = the.JIRA.get(self.url)
                self.isStart = True

            # 如果全部装载完成，则发信号
            if self.result != None:
                if len(self.result) > 0:
                    print 'finish~~~~'
                    self.ui.emit(SIGNAL(self.sign_value), self.result)
                    self.thread_stop = True
            time.sleep(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
