# -*- coding: utf-8 -*-

import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import task_ui, autos_ui
from framework.gui.models import tree_model
import base


class TaskDialog(QDialog, task_ui.Ui_Form):
    def __init__(self, data=None):
        QDialog.__init__(self)

        self.data = data

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
        # detailLayout = QGridLayout(self.widget_task)
        # taskv = QTableView()
        # detailLayout.addWidget(taskv, 0, 1)
        # self.widget_task.hide()

        # self.hzLayout.setSizeConstraint(QLayout.SetFixedSize)

        # self.btn_Automate.hide()
        self.connect(self.btn_auto, SIGNAL("clicked()"), self.select_tasks)
        self.connect(self, SIGNAL("selectTask()"), self.select_tasks)
        self.connect(self.cmb_TaskType, SIGNAL('activated(QString)'), self.onActivated)

        # u'编号', u'任务名称', u'任务类型', u'任务状态', u'优先级', u'执行人', u'创建人', u'创建时间', u'更新时间', u'执行时间', u'结束时间'
        for t in base.t.task_type:
            self.cmb_TaskType.addItem(t)

        for p in base.t.priority:
            self.cmb_TaskPriority.addItem(p)

        for ts in base.t.task_state:
            self.cmb_TaskState.addItem(ts)

        if self.data != None:
            self.setWindowTitle(u'任务编号：' + self.data[0])
            # print self.cmb_TaskType.currentText()
            self.txt_TaskName.setText(self.data[1])

            type_idx = self.cmb_TaskType.findText(self.data[2])
            self.cmb_TaskType.setCurrentIndex(type_idx)

            s_idx = self.cmb_TaskState.findText(self.data[3])
            self.cmb_TaskState.setCurrentIndex(s_idx)

            p_idx = self.cmb_TaskPriority.findText(self.data[4])
            self.cmb_TaskPriority.setCurrentIndex(p_idx)

            self.txt_executor.setText(self.data[5])
            self.lbl_creator.setText(self.data[6])
            self.lbl_createtime.setText(self.data[7])

            strBuffer = self.data[10]
            qtime = QDateTime.fromString(strBuffer, "yyyy-MM-dd hh:mm:ss")
            self.dt_endtime.setDateTime(qtime)  #(QDateTime.currentDateTime())
            self.txt_desc.setPlainText(self.data[11])#setPlainText

            if self.data[9].strip() == '':
                self.lbl_exectime_title.setText('')
                self.lbl_exectime.setText('')
            else:
                self.lbl_exectime_title.setText(u'执行时间')
                self.lbl_exectime.setText(self.data[9])
        else:
            self.setWindowTitle(u'新建任务')

            self.lbl_createtime.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))
            self.dt_endtime.setDateTime(QDateTime.currentDateTime())#(QDateTime.currentDateTime())
            self.lbl_exectime_title.setText('')
            self.lbl_exectime.setText('')


    def onActivated(self, txt):
        if txt == u'自动化':
            self.btn_auto.show()
        else:
            self.btn_auto.hide()

            # self.label.setText(txt)
            # self.label.adjustSize()

    def confirm(self):
        self.reject()  # 关闭窗口

    def select_tasks(self):
        t = SelectScriptsDialog()
        t.exec_()


class SelectScriptsDialog(QDialog, autos_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)

        # self.ui = select_task.Ui_Form()
        # self.ui.setupUi(self)
        self.setupUi(self)

        f = QFile(':/default.txt')
        f.open(QIODevice.ReadOnly)
        model = tree_model.TreeModel(f.readAll())
        f.close()
        self.treeView.setModel(model)


    def confirm(self):
        self.reject()  # 关闭窗口