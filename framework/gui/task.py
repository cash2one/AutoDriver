# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.gui.views import task_ui
from framework.gui.models import home_model
from framework.core import the
from framework.gui.helpers import temp_data
from framework.gui.dialog import dlg_task, auto_test


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

TASK_ROW = 'row'


class TaskForm(QWidget, task_ui.Ui_Form):
    def __init__(self):
        super(TaskForm, self).__init__()

        self.setupUi(self)
        self.dlgTask = None
        self.currentCellIndex = 0
        self.result_data = ()

        task_data = temp_data.task_list(PATH('../../testcase'))
        self.taskModel = home_model.QTableModel(task_data, self)

        self.createContextMenu()

        self.tv_task.setModel(self.taskModel)

        self.tv_task.setSelectionBehavior(QAbstractItemView.SelectRows)

        lastCount = self.taskModel.columnCount(self)
        self.tv_task.setColumnWidth(lastCount - 1, 400)
        self.tv_task.setAlternatingRowColors(True)
        # self.tv_task.horizontalHeader().setStretchLastSection(True)
        self.tv_task.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
        self.connect(self.tv_task, SIGNAL("doubleClicked(const QModelIndex&)"), self.show_current_task)
        self.connect(self.btn_new_task, SIGNAL("clicked()"), self.show_new_task)
        # self.connect(self.btn_temp_task, SIGNAL("clicked()"), self.show_temp_task)
        # self.connect(self, SIGNAL("finish_case"), self.show_test_result)
        # self.connect.dataChanged.connect(self.update_table)

    def update_table(self):
        self.tv_task.setModel(self.taskModel)

    def createContextMenu(self):
        '''''
        创建右键菜单
        '''
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.tv_task.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tv_task.customContextMenuRequested('const QPoint & pos').connect(self.showContextMenu)
        self.connect(self.tv_task, SIGNAL("customContextMenuRequested(const QPoint&)"), self.showContextMenu)


    def showContextMenu(self, pos):
        # 创建QMenu
        self.contextMenu = QMenu(self)
        self.actionA = self.contextMenu.addAction(u'显示详情')
        self.actionB = self.contextMenu.addAction(u'执行自动化')
        self.action_report = self.contextMenu.addAction(u'生成测试报告')
        self.actionC = self.contextMenu.addAction(u'删除')

        self.actionA.triggered.connect(self.show_current_task)
        self.actionB.triggered.connect(self.run_auto_test)
        self.actionC.triggered.connect(self.actionHandler)
        self.action_report.triggered.connect(self.startReport)
        # self.connect(self.actionB, SIGNAL("doubleClicked(const QModelIndex&)"), self.show_current_task)

        self.contextMenu.popup(QCursor.pos())
        self.contextMenu.show()

    def startReport(self):
        '''
        测试完成，生成静态html报告
        :return:
        '''
        # import webbrowser
        # from framework.core import report
        #
        # root_dir = PATH('../../')
        # rp = report.Report(data.getDatabasePath(root_dir), 25)
        # rp.start()
        # webbrowser.open(PATH('./report/index.html'))
        pass

    def run_auto_test(self):
        idx = self.tv_task.currentIndex()
        # selectionModel = self.tv_task.selectionModel()
        # indexsSelected = selectionModel.selectedIndexes()

        if idx.isValid():
            _data = self.taskModel.rowContent(idx.row())
            dlg_auto = auto_test.AutotestDialog(_data)
            if dlg_auto.exec_() == QDialog.Rejected:
                if dlg_auto.test_over:
                    row_con = _data[TASK_ROW]
                    new_row = (
                        row_con[0], row_con[1], row_con[2], u'已完成', row_con[4], row_con[5], row_con[6], row_con[7],
                        row_con[8], row_con[9], row_con[10], row_con[11])

                    self.taskModel.updateRow(new_row, idx.row())
                    self.taskModel.layoutChanged.emit()


    def actionHandler(self):
        idx = self.tv_task.currentIndex()
        # selectionModel = self.tv_task.selectionModel()
        # indexsSelected = selectionModel.selectedIndexes()

        if idx.isValid():
            _data = self.taskModel.rowContent(idx.row())
            row_con = _data[TASK_ROW]
            print row_con


    def show_current_task(self):
        idx = self.tv_task.currentIndex()
        if idx.isValid():
            self.currentCellIndex = idx.row()
            _data = self.taskModel.rowContent(self.currentCellIndex)
            # row_con = _data[TASK_ROW]

            self.dlgTask = dlg_task.TaskDialog(_data)
            # if self.dlgTask.exec_()==QDialog.Accepted:
            self.dlgTask.btn_ok.clicked.connect(self.save_current_task)
            self.dlgTask.exec_()


    def save_current_task(self):
        name = unicode(self.dlgTask.txt_TaskName.text())
        type = unicode(self.dlgTask.cmb_TaskType.currentText())
        priority = unicode(self.dlgTask.cmb_TaskPriority.currentText())
        state = unicode(self.dlgTask.cmb_TaskState.currentText())
        executor = unicode(self.dlgTask.txt_executor.text())
        creator = unicode(self.dlgTask.lbl_creator.text())
        create_time = unicode(self.dlgTask.lbl_createtime.text())
        end_time = self.dlgTask.dt_endtime.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        exec_time = self.dlgTask.lbl_exectime.text()
        update_time = QDateTime.currentDateTime()
        desc = unicode(self.dlgTask.txt_desc.toPlainText())
        # u'编号', u'任务名称', u'任务类型', u'任务状态', u'优先级', u'执行人', u'创建人', u'创建时间', u'更新时间', u'执行时间', u'结束时间'
        current_data = self.taskModel.rowContent(self.currentCellIndex)
        task_no = current_data['row'][0]

        new_data = (
            task_no, name, type, state, priority, executor, creator, create_time, update_time, exec_time, end_time,
            desc)
        self.taskModel.updateRow(new_data, self.currentCellIndex)

        self.taskModel.layoutChanged.emit()
        self.dlgTask.reject()


    def show_new_task(self):
        if the.jira.isActive:
            self.dlgTask = dlg_task.TaskDialog()
            self.dlgTask.lbl_creator.setText(the.jira.userName)
            self.dlgTask.btn_ok.clicked.connect(self.insert_data)
            self.dlgTask.exec_()
        else:
            ret = QMessageBox.warning(self, u'未登录',
                                      u"\n你还没有登录JIRA，点击确定登录  \n",
                                      QMessageBox.Yes | QMessageBox.Cancel)
            if ret == QMessageBox.Yes:
                self.emit(SIGNAL("notLogin"))
            elif ret == QMessageBox.Cancel:
                pass


    def insert_data(self):
        name = unicode(self.dlgTask.txt_TaskName.text())
        type = unicode(self.dlgTask.cmb_TaskType.currentText())
        priority = unicode(self.dlgTask.cmb_TaskPriority.currentText())
        state = unicode(self.dlgTask.cmb_TaskState.currentText())
        executor = unicode(self.dlgTask.txt_executor.text())
        creator = unicode(self.dlgTask.lbl_creator.text())
        create_time = unicode(self.dlgTask.lbl_createtime.text())
        desc = unicode(self.dlgTask.txt_desc.toPlainText())
        end_time = self.dlgTask.dt_endtime.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        exec_time = ''
        update_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        current_data = self.taskModel.rowContent(self.currentCellIndex)
        task_no = current_data['row'][0]

        new_data = {
            'row': (
                task_no, name, type, state, priority, executor, creator, create_time, update_time, exec_time, end_time,
                desc),
            'task': []}

        p_idx = self.dlgTask.cmb_TaskPriority.currentIndex()
        t_idx = self.dlgTask.cmb_TaskType.currentIndex()
        ts_idx = self.dlgTask.cmb_TaskState.currentIndex()
        t_name = self.dlgTask.txt_TaskName.text()
        if p_idx > 0 and t_idx > 0 and ts_idx > 0 and not QString(t_name).isEmpty():
            print self.dlgTask.cmb_TaskPriority.currentIndex()
            self.taskModel.insertRows(new_data)
            self.taskModel.layoutChanged.emit()
            self.dlgTask.reject()
        else:
            QMessageBox.warning(self, u'内容不完整',
                                u"\n有未填写的内容，请仔细校对！  \n",
                                QMessageBox.Yes)

