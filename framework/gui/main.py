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

        self.connect(self.menu_login, SIGNAL(("triggered()")), self.login_dialog)
        self.connect(self.toolbar_home, SIGNAL(("triggered()")), self.load_index)
        self.connect(self.toolbar_jira, SIGNAL("triggered()"), self.load_jira)
        self.statusBar().showMessage(u'未登录')
        self.load_index()


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

    def load_jira(self):
        if the.JIRA == None:
            self.msgHandler()
            return

        if the.JIRA.isActive:
            self.frm_jira = form.JIRAForm()
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
