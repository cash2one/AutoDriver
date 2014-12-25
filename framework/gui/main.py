# -*- coding: utf-8 -*-

import sys
import time
import threading

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import main_window, ui_test2, ui_test3, index, login_ja, select_task

from framework.core import the

import task,login,home,jira_main


class MainWindow(QMainWindow, main_window.Ui_MainWindow):

    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # self.widget

        self.index_widget = None
        self.jm=None

        self.connect(self.action_JIRA, SIGNAL(("triggered()")), self.login_dialog)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.load_index)
        #self.connect(self.pushButton_2, SIGNAL("clicked()"), self.btn2_click)
        self.connect(self.pushButton_3, SIGNAL("clicked()"), self.load_jira)

        self.load_index()

    # 打开第一个窗口
    def load_index(self):
        self.index_widget = home.MainForm(self.widget)
        #index_main.signal()
        self.index_widget.connect(self.index_widget.pushButton, SIGNAL("clicked()"), self.new_task)
        self.index_widget.table_task.cellDoubleClicked.connect(self.select_tasks)


    # 打开第二个窗口
    def btn2_click(self):
        self.initMainWinEvent()
        self.secondUi = ui_test2.Ui_Form()
        w2 = QWidget(self.widget)
        self.secondUi.setupUi(w2)

        project = 'IDRIVERC'
        start = '10'
        end = '20'
        if the.JIRA != None:
            p = the.JIRA.get(
                '/rest/api/2/search?jql=project+%3D+' + project + '&startAt=' + start + '&maxResults=' + end)

            self.secondUi.label.setText(str(p['maxResults']))

    # 打开第三个窗口
    def load_jira(self):
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
    #     self.setupUi(self)
    #     # if the.JIRA!=None:
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
