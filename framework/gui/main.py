# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import main_window_ui
from framework.core import the
import form, dialog


class MainWindow(QMainWindow, main_window_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # self.widget

        self.frm_home = None
        self.frm_jira = None
        self.dlg_login = None
        self.dlg_select_task = None
        self.dlg_new_task = None
        self.dlg_task=None
        self.tasks=None
        self.menu_login.triggered.connect(self.login_dialog)
        #self.connect(self.menu_login, SIGNAL(("triggered()")), self.login_dialog)
        self.connect(self.toolbar_home, SIGNAL(("triggered()")), self.load_index)
        self.connect(self.toolbar_jira, SIGNAL("triggered()"), self.load_jira)

        #显示托盘信息
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("./ui/res/wp.ico"))
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.trayClick)       #点击托盘
        self.trayMenu()#右键菜单

        self.setFont(QFont("Microsoft YaHei", 10))
        self.showMaximized()
        self.load_index()

    def trayMenu(self):
       #右击托盘弹出的菜单
       img_main = QIcon("./ui/res/app.png")
       img_exit = QIcon("./ui/res/exit.png")
       self.trayIcon.setToolTip(u'Autotest')
       self.restoreAction = QAction(img_main,u"打开主窗口", self)
       self.restoreAction.triggered.connect(self.showNormal)
       self.quitAction = QAction(img_exit,u"退出", self)
       self.quitAction.triggered.connect(qApp.quit)
       self.trayIconMenu = QMenu(self)
       self.trayIconMenu.addAction(self.restoreAction)
       self.trayIconMenu.addSeparator()
       self.trayIconMenu.addAction(self.quitAction)
       self.trayIcon.setContextMenu(self.trayIconMenu)

    def load_index(self):
        self.tasks = ({'info': (u'001', u'测试用户端', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-22'), 'autos': []},
                 {'info': (u'002', u'测试司机端', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-23'), 'autos': []})
        self.frm_home = form.HomeForm(self.tasks)
        self.frm_home.connect(self.frm_home.pushButton, SIGNAL("clicked()"), self.new_task)
        self.frm_home.table_task.cellDoubleClicked.connect(self.show_current_task)
        #self.connect(self.frm_home.table_task, SIGNAL("itemDoubleClicked(QTableWidgetItem*)"), self.outSelect)
        #self.self.frm_home.table_task.cellChanged.connect(self.makeDirty)
        self.setCentralWidget(self.frm_home)

    def outSelect(self, Item=None):
        if Item == None:
            return
        print(unicode(Item))

    def trayClick(self,reason):
        if reason==QSystemTrayIcon.DoubleClick:
            print 'fff'
            self.showNormal()
        else:
            pass


    def showMessage(self):
        icon=QSystemTrayIcon.Information

        self.trayicon.showMessage(u" 提示信息 ",u" 点我干嘛？ ",icon)

    def load_jira(self):
        if the.JIRA == None:
            self.msgHandler()
            return

        if the.JIRA.isActive:
            ddd=the.JIRA.get('/rest/api/2/search?jql=project{0}&startAt={1}&maxResults={2}' %('BVAL','10','20'))

            self.frm_jira = form.JIRAForm(ddd)
            self.setCentralWidget(self.frm_jira)


        else:
            self.msgHandler()


    def msgHandler(self):
        ret = QMessageBox.warning(self, u'未登录',
                                  u"\n还没有登录JIRA，点击文件菜单登录  \n",
                                  QMessageBox.Save | QMessageBox.Cancel)
        if ret == QMessageBox.Save:
            pass
        elif ret == QMessageBox.Cancel:
            pass



    # 通过单击第一个窗口里的按钮，弹出第四个窗口
    def login_dialog(self):
        if the.JIRA != None:
            if the.JIRA.isActive:
                return

        if self.dlg_login == None:
            self.dlg_login = dialog.LoginDialog()
        self.dlg_login.exec_()

    def show_msg(self, txt):
        msg = dialog.MsgDialog(txt)
        msg.exec_()

    # def select_tasks(self):
    #     if self.dlg_select_task == None:
    #         self.dlg_select_task = dialog.SelectTaskDialog()
    #     self.dlg_select_task.exec_()

    def new_task(self):
        print self.frm_home.table_task.currentRow()
        if self.dlg_new_task == None:
            self.dlg_new_task = dialog.TaskDialog()
        self.dlg_new_task.exec_()

    def show_current_task(self):
        current_row = self.frm_home.table_task.currentRow()
        row_data = self.tasks[current_row]['info']
        if self.dlg_task == None:
            self.dlg_task = dialog.TaskDialog()


        self.dlg_task.txt_TaskName.setText(row_data[1])
        self.dlg_task.txt_Creator.setText(row_data[5])
        self.dlg_task.exec_()




        # # 初始化主界面，进行按钮的动态绑定
        # def initMainWinEvent(self):
        # self.setupUi(self)
        # # if the.JIRA!=None:
        # #     self.statusBar().showMessage(the.JIRA.dislayName)
        # self.connect(self.action_JIRA, SIGNAL(("triggered()")), self.login_dialog)
        # self.connect(self.pushButton, SIGNAL("clicked()"), self.load_index)
        # self.connect(self.pushButton_2, SIGNAL("clicked()"), self.btn2_click)
        # self.connect(self.pushButton_3, SIGNAL("clicked()"), self.btn3_click)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
