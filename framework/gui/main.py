# -*- coding: utf-8 -*-

import sys
import time
import threading

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import main_window_ui
import task, login, home, jira_main


class MainWindow(QMainWindow, main_window_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # self.widget

        self.index_widget = None
        self.jm = None

        self.connect(self.action_JIRA, SIGNAL(("triggered()")), self.login_dialog)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.load_index)
        self.connect(self.pushButton_3, SIGNAL("clicked()"), self.load_jira)

        self.load_index()


    def load_index(self):
        if self.index_widget==None:
            self.index_widget = home.MainForm(self.widget)
            # index_main.signal()
        self.index_widget.connect(self.index_widget.pushButton, SIGNAL("clicked()"), self.new_task)
        self.index_widget.table_task.cellDoubleClicked.connect(self.select_tasks)

    def load_jira(self):
        if self.jm==None:
            self.jm = jira_main.MainForm(self.widget)

    # 通过单击第一个窗口里的按钮，弹出第四个窗口
    def login_dialog(self):
        lg = login.MainDialog()
        lg.exec_()

    def select_tasks(self):
        t = task.SelectAutomate()
        t.exec_()

    def new_task(self):
        t = task.New()
        t.exec_()


        # # 初始化主界面，进行按钮的动态绑定
        # def initMainWinEvent(self):
        # self.setupUi(self)
        # # if the.JIRA!=None:
        #     #     self.statusBar().showMessage(the.JIRA.dislayName)
        #     self.connect(self.action_JIRA, SIGNAL(("triggered()")), self.login_dialog)
        #     self.connect(self.pushButton, SIGNAL("clicked()"), self.load_index)
        #     self.connect(self.pushButton_2, SIGNAL("clicked()"), self.btn2_click)
        #     self.connect(self.pushButton_3, SIGNAL("clicked()"), self.btn3_click)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
