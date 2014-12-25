# coding=utf-8
__author__ = 'Administrator'

import os
import sys
import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import task

from framework.gui.ui import index


class MainForm(QWidget, index.Ui_Form):
    def __init__(self, parent_widget):
        super(MainForm, self).__init__()

        self.setupUi(parent_widget)

        self.table_task.setHorizontalHeaderLabels([u'编号', u'任务名称', u'任务状态', u'任务类型',
                                                   u'优先级', u'执行人', u'创建人', u'创建时间'])
        self.table_task.setVerticalHeaderLabels(['1', '2', '3', '4',
                                                 '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
        self.table_task.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_task.setEditTriggers(QTableWidget.NoEditTriggers)

        table_rows = self.table_task.rowCount()
        table_cols = self.table_task.columnCount()
        for i in range(table_rows):
            for j in range(table_cols):
                cnt = '(%d,%d)' % (i, j)
                newItem = QTableWidgetItem(cnt)
                self.table_task.setItem(i, j, newItem)

    def signal(self):
        # self.connect(self.pushButton, SIGNAL("clicked()"), self.login_dialog)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.select_tasks)
        self.table_task.cellDoubleClicked.connect(self.select_tasks)

    def select_tasks(self):
        t = task.SelectTaskDialog()
        t.exec_()