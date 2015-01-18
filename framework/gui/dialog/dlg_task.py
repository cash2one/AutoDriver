# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.util import const
from framework.gui.views import dlg_task_ui
from framework.gui.models import script_model
from framework.gui.dialog import check_user, script_list

GUI_TASK_TYPE = (u'自动化', u'车机测试', u'App', u'Web平台', u'接口', u'性能测试')
GUI_TASK_PRIORITY = (u'普通', u'中级', u'高级')
GUI_TASK_STATE = (u'未开始', u'已开始', u'已取消', u'已结束')


class TaskDialog(QDialog, dlg_task_ui.Ui_Form):
    def __init__(self, data=None):
        QDialog.__init__(self)

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
        self.current_executor = []

        self.connect(self.btn_auto, SIGNAL("clicked()"), self.select_tasks)
        self.connect(self, SIGNAL("selectTask()"), self.select_tasks)
        self.connect(self.cmb_TaskType, SIGNAL('activated(QString)'), self.onActivated)
        self.btn_requester.clicked.connect(self.select_user)

        self.data_row = None
        if data != None:
            self.data_row = data['row']
            self.data_task = data['task']

            if len(self.data_task) > 0:
                tv_detail, tab_detail_layout = self.add_tab(u'任务详情')
                tv_detail = QTableView()
                tv_detail.setFrameShape(QFrame.NoFrame)
                print 'cases:', self.data_task[0]['cases']
                print 'result:', self.data_task[0]['result']
                print 'status:', self.data_task[0]['status']
                print 'path:', self.data_task[0]['path']
                t_model = script_model.QTableModel(self.data_task[0]['cases'], self)
                tv_detail.setModel(t_model)
                tv_detail.setColumnWidth(0, 250)
                tv_detail.horizontalHeader().setStretchLastSection(True)

                tab_detail_layout.addWidget(tv_detail)

        for t in GUI_TASK_TYPE:
            self.cmb_TaskType.addItem(t)

        for p in GUI_TASK_PRIORITY:
            self.cmb_TaskPriority.addItem(p)

        for ts in GUI_TASK_STATE:
            self.cmb_TaskState.addItem(ts)

        if self.data_row != None:
            self.setWindowTitle(u'任务编号：' + self.data_row[0])
            # print self.cmb_TaskType.currentText()
            self.txt_TaskName.setText(self.data_row[1])

            type_idx = self.cmb_TaskType.findText(self.data_row[2])
            self.cmb_TaskType.setCurrentIndex(type_idx)

            if self.data_row[2] == u'自动化':
                self.btn_auto.show()
            else:
                self.btn_auto.hide()

            s_idx = self.cmb_TaskState.findText(self.data_row[3])
            self.cmb_TaskState.setCurrentIndex(s_idx)

            p_idx = self.cmb_TaskPriority.findText(self.data_row[4])
            self.cmb_TaskPriority.setCurrentIndex(p_idx)

            self.txt_executor.setText(self.data_row[5])
            self.lbl_creator.setText(self.data_row[6])
            self.lbl_createtime.setText(self.data_row[7])

            strBuffer = self.data_row[10]
            qtime = QDateTime.fromString(strBuffer, "yyyy-MM-dd hh:mm:ss")
            self.dt_endtime.setDateTime(qtime)  # (QDateTime.currentDateTime())
            self.txt_desc.setPlainText(self.data_row[11])  # setPlainText

            if QString(self.data_row[9]).isEmpty():
                self.lbl_exectime_title.setText('')
                self.lbl_exectime.setText('')
            else:
                self.lbl_exectime_title.setText(u'执行时间')
                self.lbl_exectime.setText(self.data_row[9])
        else:
            self.setWindowTitle(u'新建任务')

            self.lbl_createtime.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))
            self.dt_endtime.setDateTime(QDateTime.currentDateTime())  # (QDateTime.currentDateTime())
            self.btn_auto.hide()
            self.lbl_exectime_title.setText('')
            self.lbl_exectime.setText('')


    def onActivated(self, txt):
        if txt == u'自动化':
            self.btn_auto.show()
        else:
            self.btn_auto.hide()

    def confirm(self):
        self.reject()

    def add_tab(self, tab_name):
        tab_detail = QWidget()
        # self.tab_detail.setObjectName(_fromUtf8("tab_detail"))
        tab_detail_layout = QVBoxLayout(tab_detail)
        tab_detail_layout.setSpacing(0)
        tab_detail_layout.setMargin(0)
        # self.tab_detail_layout.setObjectName(_fromUtf8("tab_detail_layout"))
        # self.tw_task.setTabText(self.tw_task.indexOf(tab_detail),u'任务详情')
        self.tw_task.addTab(tab_detail, tab_name)
        return tab_detail, tab_detail_layout


    def select_tasks(self):
        t = script_list.ScriptsDialog()
        t.exec_()

    def select_user(self):
        self.selectUser = check_user.UserDialog()
        self.current_executor = self.txt_executor.text().split(';')
        print self.current_executor
        # self.selectUser.lbl_creator.setText(self.user)
        # self.selectUser.btn_ok.clicked.connect(self.insert_data)

        if self.selectUser.exec_():
            print self.selectUser.getUser()
            # self.model.appendRow((
            # QStandardItem(self.selectUser.name()),
            # QStandardItem(str(self.selectUser.age())),
            # ))

        self.selectUser.destroy()
