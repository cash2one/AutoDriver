# coding=utf-8
__author__ = 'guguohai@outlook.com'

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtNetwork

from framework.core import box
from woodpecker.views import main_ui
from woodpecker.dialog import monitor, new_issue, car_service
import task
import jiras
import api_test
import testcase,login,home,recording


ja = box.jira


class MainWindow(QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        ja.cookie = QtNetwork.QNetworkCookieJar(self)

        self.setFont(QFont("Microsoft YaHei", 10))
        self.showMaximized()
        self.statusBar().showMessage(self.tr("Parsing eventlog data..."))

        self.dlg_login = None
        self.dlg_select_task = None
        self.dlg_new_task = None
        self.dlg_task = None

        self.connect(self.menu_login, SIGNAL("triggered()"), self.login_dialog)
        # self.connect(self.menu_login, SIGNAL(("triggered()")), self.login_dialog)
        self.connect(self.toolbar_home, SIGNAL(("triggered()")), self.load_index)
        self.connect(self.toolbar_jira, SIGNAL("triggered()"), self.load_jira_main)
        self.connect(self, SIGNAL("startLogin()"), self.login_dialog)
        self.toolbar_case.triggered.connect(self.load_testcase)
        self.toolbar_task.triggered.connect(self.load_task)
        self.toolbar_knowledge.triggered.connect(self.show_knowledge)
        self.toolbar_interface.triggered.connect(self.show_interface)
        self.toolbar_monitor.triggered.connect(self.show_monitor)
        self.toolbar_car.triggered.connect(self.show_car_service)
        self.toolbar_script.triggered.connect(self.show_recording)

        # 显示托盘信息
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("./views/res/wp.ico"))
        self.trayIcon.show()
        self.connect(self.trayIcon, SIGNAL("activated()"), self.trayClick)
        # self.trayIcon.activated.connect(self.trayClick) #点击托盘
        self.trayMenu()  # 右键菜单

        self.msg_btn_ok = QPushButton("OK")
        self.msg_btn_cancel = QPushButton("Cancel")

        #self.load_index()

    def save_task(self, arg):
        self.task_data += arg
        print self.task_data

    def add_widget(self, form):
        # frm_testcase = testcase.TestCaseForm()
        wid = QWidget()
        vlayout = QVBoxLayout(wid)
        vlayout.setSpacing(0)
        vlayout.setMargin(0)
        vlayout.addWidget(form)
        self.setCentralWidget(wid)

    def update_user(self, arg):
        self.toolbar_jira.setText(arg.capitalize())

    def trayMenu(self):
        # 右击托盘弹出的菜单
        img_main = QIcon("./views/res/app.png")
        img_exit = QIcon("./views/res/exit.png")
        self.trayIcon.setToolTip(u'Woodpecker')
        self.restoreAction = QAction(img_main, u"打开主窗口", self)
        self.restoreAction.triggered.connect(self.showMaximized)
        self.quitAction = QAction(img_exit, u"退出", self)
        self.quitAction.triggered.connect(qApp.quit)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu)

    def load_index(self):
        # na = [self.netAccessNoCookie, self.netAccessNoCookie]
        frm_home = home.HomeForm()
        # frm_home.connect(frm_home, SIGNAL("notLogin"), self.login_dialog)
        #self.setCentralWidget(self.frm_home)
        self.add_widget(frm_home)


    def load_testcase(self):
        # self.frm_testcase = testcase.TestCaseForm()
        # self.setCentralWidget(self.frm_testcase)
        frm_testcase = testcase.TestCaseForm()
        #self.setCentralWidget(self.frm_testcase)
        self.add_widget(frm_testcase)


    def load_task(self):
        frm_task = task.TaskForm()
        frm_task.connect(frm_task, SIGNAL("notLogin"), self.login_dialog)
        self.setCentralWidget(frm_task)


    def outSelect(self, Item=None):
        if Item == None:
            return
        print(unicode(Item))


    def trayClick(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showNormal()
        else:
            pass

    def netAccess(self, api, reply_func):
        m1 = QtNetwork.QNetworkAccessManager(self)
        m1.setCookieJar(ja.cookie)
        m1.finished.connect(reply_func)
        req1 = QtNetwork.QNetworkRequest(QUrl(api))
        m1.get(req1)

    # def netAccessNoCookie(self, url, reply_func):
    # m = QtNetwork.QNetworkAccessManager(self)
    # # m1.setCookieJar(ja.cookie)
    #     m.finished.connect(reply_func)
    #     req = QtNetwork.QNetworkRequest(QUrl(url))
    #     # req.setRawHeader("Host", "www.nuihq.com")
    #     req.setRawHeader("User-Agent",
    #                      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")
    #     req.setRawHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    #     # req.setRawHeader("Accept-Language", "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4")
    #     # req.setRawHeader("Accept-Encoding", "deflate")
    #     # req.setRawHeader("Accept-Charset", "utf-8;q=0.7,*;q=0.7")
    #     # req.setRawHeader("Connection", "keep-alive")
    #     # req.setRawHeader("Accept-Encoding", "gzip, deflate, sdch")
    #     m.get(req)

    def load_jira_main(self):
        if ja.isActive:
            frm_jira = jiras.JIRAForm(self.netAccess)
            self.setCentralWidget(frm_jira)
        else:
            self.msgHandler()


    def msgHandler(self):
        ret = QMessageBox.warning(self, u'未登录',
                                  u"\n你还没有登录JIRA，点击确定登录",
                                  QMessageBox.Yes | QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.emit(SIGNAL("startLogin()"))
        elif ret == QMessageBox.Cancel:
            pass

    def login_dialog(self):
        if ja.isActive:
            return

        if self.dlg_login == None:
            self.dlg_login = login.LoginDialog()
            self.connect(self.dlg_login, SIGNAL("loginFinish"), self.update_user)
        self.dlg_login.exec_()

    def show_monitor(self):
        monitorDlg = monitor.MonitorDialog()
        monitorDlg.exec_()


    def show_knowledge(self):
        issueDlg = new_issue.IssueDialog()
        if issueDlg.exec_() == QDialog.Accepted:
            print unicode(issueDlg.label.text())
        else:
            pass

    def show_interface(self):
        interfaceDlg = api_test.InterfaceForm()
        self.setCentralWidget(interfaceDlg)

    def show_recording(self):
        record = recording.RecordingForm()
        self.setCentralWidget(record)

    def show_car_service(self):
        dlg_car = car_service.CarServiceDialog()
        dlg_car.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
