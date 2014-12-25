# -*- coding: utf-8 -*-

import sys
import time
import threading

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import main_window, ui_test2, ui_test3, index, login_ja, select_task

from framework.core import the

import task,login


class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    firstUi = None
    secondUi = None
    thridUi = None

    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # self.widget
        #self.centralwidget

        self.load_index()

    # 打开第一个窗口
    def load_index(self):
        # self.form=idx.MainForm()
        # self.form.show()

        self.initMainWinEvent()  # 初始化主界面的事件
        self.firstUi = index.Ui_Form()
        w1 = QWidget(self.widget)
        self.firstUi.setupUi(w1)

        self.firstUi.table_task.setHorizontalHeaderLabels([u'编号', u'任务名称', u'任务状态', u'任务类型',
                                                           u'优先级', u'执行人', u'创建人', u'创建时间'])
        self.firstUi.table_task.setVerticalHeaderLabels(['1', '2', '3', '4',
                                                         '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
        self.firstUi.table_task.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.firstUi.table_task.setEditTriggers(QTableWidget.NoEditTriggers)

        table_rows = self.firstUi.table_task.rowCount()
        table_cols = self.firstUi.table_task.columnCount()
        for i in range(table_rows):
            for j in range(table_cols):
                cnt = '(%d,%d)' % (i, j)
                newItem = QTableWidgetItem(cnt)
                self.firstUi.table_task.setItem(i, j, newItem)

        # self.connect(self.firstUi.pushButton, SIGNAL("clicked()"), self.login_dialog)
        self.connect(self.firstUi.pushButton, SIGNAL("clicked()"), self.select_tasks)
        self.firstUi.table_task.cellDoubleClicked.connect(self.select_tasks)

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
    def btn3_click(self):
        self.initMainWinEvent()
        # 将窗体定义成类成员变量
        self.thridUi = ui_test3.Ui_Form()
        w3 = QWidget(self.widget)
        self.thridUi.setupUi(w3)

    # 通过单击第一个窗口里的按钮，弹出第四个窗口
    def login_dialog(self):
        lg = login.MainDialog()
        lg.exec_()

    def select_tasks(self):
        t = task.SelectAutomate()
        t.exec_()


    # 初始化主界面，进行按钮的动态绑定
    def initMainWinEvent(self):
        self.setupUi(self)
        # if the.JIRA!=None:
        #     self.statusBar().showMessage(the.JIRA.dislayName)
        self.connect(self.action_JIRA, SIGNAL(("triggered()")), self.login_dialog)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.load_index)
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.btn2_click)
        self.connect(self.pushButton_3, SIGNAL("clicked()"), self.btn3_click)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
