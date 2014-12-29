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
from framework.gui.ui import jira_main_ui


class MainForm(QWidget, jira_main_ui.Ui_Form):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setupUi(self)

        self.tv_bugs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_bugs.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tv_bugs.setAlternatingRowColors(True)

        # self.connect(self, SIGNAL("jiraHomeComplete()"), self.setTableModel)

        lnd = LoadNetData(self, the.JIRA)
        lnd.start()
        #the.JIRA.project = the.JIRA.getProject()
        # if the.JIRA.project != None:
        #     for key in the.JIRA.project:
        #         self.cmb_project.addItem(key)
        # tablemodel = jira_model.MyTableModel(self.task_data, self)
        # self.tv_bugs.setModel(tablemodel)
        # self.tv_bugs.setColumnWidth(0, 200)
        # self.tv_bugs.setColumnWidth(1, 400)
        # self.tv_bugs.setColumnWidth(1, 200)
        # self.tv_bugs.setColumnWidth(1, 200)
        # print self.getData('IDRIVERC',10,20)


class LoadNetData(threading.Thread):
    def __init__(self, ui, jira):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.ui = ui
        self.jira = jira
        the.JIRA.home_data = None

    def run(self):
        while not self.thread_stop:
            if not self.jira.isActive:
                print u'未登录!'
            else:
                if the.JIRA.home_data != None:
                    print 'sendsign~~'
                    self.ui.emit(SIGNAL("jiraHomeComplete()"))
                    self.stop()
                else:
                    the.JIRA.home_data = the.JIRA.getJiraHome('IDRIVERC', '10', '20')
                    print 'jjj:', the.JIRA.home_data
            time.sleep(1)

    def stop(self):
        self.thread_stop = True