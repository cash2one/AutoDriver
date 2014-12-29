# coding=utf-8
__author__ = 'Administrator'

import os
import sys
import re
import time
import threading
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.core import the
from framework.gui.ui import home_ui, jira_main_ui
from framework.gui.models import table_model, jira_model

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeForm(QWidget, home_ui.Ui_Form):
    '''
    首页
    '''

    def __init__(self, task_data):
        super(HomeForm, self).__init__()

        self.setupUi(self)
        self.task_data = task_data
        self.table_task.setHorizontalHeaderLabels([u'编号', u'任务名称', u'任务状态', u'任务类型',
                                                   u'优先级', u'执行人', u'创建人', u'创建时间'])

        self.show_files()

        self.table_task.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_task.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table_task.setAlternatingRowColors(True)


        # table_rows = self.table_task.rowCount()
        # table_cols = self.table_task.columnCount()
        self.table_task.setColumnWidth(1, 300)

        for ts in range(0, len(self.task_data)):
            infos = self.task_data[ts]['info']
            for t in range(0, len(infos)):
                newItem = QTableWidgetItem(infos[t])
                self.table_task.setItem(ts, t, newItem)



                # def signal(self):
                # # self.connect(self.pushButton, SIGNAL("clicked()"), self.login_dialog)
                # self.connect(self.pushButton, SIGNAL("clicked()"), self.select_tasks)
                # self.table_task.cellDoubleClicked.connect(self.select_tasks)
                #
                # def select_tasks(self):
                # t = task.SelectTaskDialog()
                #     t.exec_()

    def show_files(self):
        tablemodel = table_model.MyTableModel(self.task_data, self)
        # tablemodel.setHorizontalHeaderLabels([u'编号', u'任务名称', u'任务状态', u'任务类型',
        # u'优先级', u'执行人', u'创建人', u'创建时间'])

        tablemodel.setHeaderData(0, Qt.Horizontal, QVariant("ID"))
        tablemodel.setHeaderData(1, Qt.Horizontal, QVariant("File Order"))
        tablemodel.setHeaderData(2, Qt.Horizontal, QVariant("Type"))
        tablemodel.setHeaderData(3, Qt.Horizontal, QVariant("Name"))
        tablemodel.setHeaderData(4, Qt.Horizontal, QVariant("Presort Name"))
        tablemodel.setHeaderData(5, Qt.Horizontal, QVariant("Record"))

        self.tv_task.setModel(tablemodel)
        # #水平表头
        # head = QHeaderView(Qt.Horizontal, self)
        # #自定义模式，不能拖动
        # #head.setResizeMode(QHeaderView.Custom)
        # head.resizeSection(0,30)
        # head.resizeSection(1,300)
        # head.resizeSection(2,160)
        # head.resizeSection(3,70)

        # self.tv_task.setHorizontalHeader(head)
        # self.tv_task.setColumnHidden(1, True)
        self.tv_task.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_task.setColumnWidth(1, 300)
        self.tv_task.setAlternatingRowColors(True)
        # self.tv_task.setHorizontalHeaderLabels([u'编号', u'任务名称', u'任务状态', u'任务类型',
        #                                            u'优先级', u'执行人', u'创建人', u'创建时间'])
        self.tv_task.horizontalHeader().setStretchLastSection(True)



        #self.table_task.show()

    def delRow(self, data):
        self.table_task.removeRow()

    def insertRow(self, data):
        self.table_task.insertRow()


class JIRAForm(QWidget, jira_main_ui.Ui_Form):
    '''
    JIRA
    '''

    def __init__(self):
        super(JIRAForm, self).__init__()

        self.setupUi(self)

        self.tv_bugs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_bugs.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tv_bugs.setAlternatingRowColors(True)

        self.connect(self, SIGNAL("jiraHomeComplete()"), self.setTableModel)

        the.JIRA.project = the.JIRA.getProject()
        lnd = LoadNetData(self, the.JIRA)
        lnd.start()

        if the.JIRA.project != None:
            for key in the.JIRA.project:
                self.cmb_project.addItem(key)
                # tablemodel = jira_model.MyTableModel(self.task_data, self)
                # self.tv_bugs.setModel(tablemodel)
                # self.tv_bugs.setColumnWidth(0, 200)
                # self.tv_bugs.setColumnWidth(1, 400)
                # self.tv_bugs.setColumnWidth(1, 200)
                # self.tv_bugs.setColumnWidth(1, 200)
                # print self.getData('IDRIVERC',10,20)

    def setTableModel(self):
        tablemodel = jira_model.MyTableModel(the.JIRA.home_data, self)
        self.tv_bugs.setModel(tablemodel)



class LoadNetData(threading.Thread):
    def __init__(self, ui, jira):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.ui = ui
        self.jira = jira
        the.JIRA.home_data = None
        # self.startLogin = False

    def run(self):
        while not self.thread_stop:
            if not self.jira.isActive:
                print u'未登录!'
            else:
                if the.JIRA.home_data != None:
                    self.ui.emit(SIGNAL("jiraHomeComplete()"))
                    self.stop()
                else:
                    the.JIRA.home_data = the.JIRA.getJiraHome('IDRIVERC', '10', '20')
                    print 'jjj:',the.JIRA.home_data
            time.sleep(1)

    def stop(self):
        self.thread_stop = True