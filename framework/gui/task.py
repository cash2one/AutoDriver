# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.util import fs
from framework.gui.views import task_ui
from framework.gui.models import home_model
from framework.core import the
from framework.gui.dialog import dlg_task, temp_task


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

        task_datas = (
            {'row': (
                u'001', u'接口测试', u'自动化', u'未开始', u'普通', u'顾国海', u'顾国海', u'2014-07-02 17:35:00', u'2014-07-02 17:35:00',
                u'2014-07-02 17:35:00',
                u'2014-07-02 17:35:00', 'desc'), 'script': []},
            {'row': (
                u'002', u'app平台测试', u'自动化', u'未开始', u'高级', u'顾国海', u'顾国海', u'2014-08-02 17:35:00',
                u'2014-08-02 17:35:00', u'2014-08-02 17:35:00',
                u'2014-08-02 17:35:00', 'desc'),
             'script': []})

        self.taskModel = home_model.QTableModel(task_datas, self)
        self.createContextMenu()

        self.tv_task.setModel(self.taskModel)

        self.tv_task.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_task.setColumnWidth(1, 300)
        self.tv_task.setAlternatingRowColors(True)
        self.tv_task.horizontalHeader().setStretchLastSection(True)
        self.connect(self.tv_task, SIGNAL("doubleClicked(const QModelIndex&)"), self.show_current_task)
        self.connect(self.btn_new_task, SIGNAL("clicked()"), self.show_new_task)
        self.connect(self.btn_temp_task, SIGNAL("clicked()"), self.show_temp_task)

        # self.connect.dataChanged.connect(self.update_table)

    def update_table(self):
        self.tv_task.setModel(self.taskModel)

    def createContextMenu(self):
        '''''
        创建右键菜单
        '''
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        # 创建QMenu
        self.contextMenu = QMenu(self)
        self.actionA = self.contextMenu.addAction(u'显示详情')
        self.actionB = self.contextMenu.addAction(u'执行自动化')
        self.actionC = self.contextMenu.addAction(u'删除')

        self.actionA.triggered.connect(self.actionHandler)
        self.actionB.triggered.connect(self.actionHandler)
        self.actionB.triggered.connect(self.actionHandler)

    def showContextMenu(self, pos):
        self.contextMenu.popup(QCursor.pos())
        self.contextMenu.show()

    def actionHandler(self):
        idx = self.tv_task.currentIndex()
        if idx.isValid():
            _data = self.taskModel.rowContent(idx.row())
            row_con = _data[TASK_ROW]
            print row_con


    def show_current_task(self):
        idx = self.tv_task.currentIndex()
        if idx.isValid():
            self.currentCellIndex = idx.row()
            _data = self.taskModel.rowContent(self.currentCellIndex)
            row_con = _data[TASK_ROW]

            self.dlgTask = dlg_task.TaskDialog(row_con)
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
        # createUser=''
        # createTime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # if self.data!=None:
        # createUser = self.data.displayName

        # strBuffer = self.data[10]
        # qtime = QDateTime.fromString(strBuffer, "yyyy-MM-dd hh:mm:ss")
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

    def show_temp_task(self):
        dlg = temp_task.TaskExecDialog()
        case_path = PATH('../../testcase/')

        case_list = []
        if dlg.exec_() == QDialog.Accepted:
            for i in reversed(range(0, dlg.folderLayout.count())):
                chk = dlg.folderLayout.itemAt(i).widget()
                case_f = {}
                if chk.isChecked():
                    p = dlg.chk_value[i]
                    print p
                    #case_s = os.listdir(p)
                    case_dict = {}  # 取出文件夹内的用例，并设置执行次数

                    files = fs.filter_files(p,'test','py')

                    for c in files:
                        case_dict[c] = 1
                    case_f['cases'] = case_dict
                    case_f['status'] = 0
                    case_f['path'] = p#p[len(PATH('../../'))+1:len(p)]
                    case_list.append(case_f)
        self.start_task(case_list)
        #print case_list


    def start_task(self, case_list):
        from framework.core import task as ta
        # case_list = [
        # {'cases': {'test_customer_allfinishOrder': 5, 'test_customer_callServer_xgh': 3}, 'status': 0,
        # 'path': 'testcase/AutobookClient/customer'},
        # {'cases': {'test_driver_cmEarnings_zc': 3, 'test_driver_completeOrder_info__zc': 2}, 'status': 0,
        #      'path': 'testcase/AutobookClient/driver'}
        # ]

        task_list = []
        for c in case_list:
            print c
            t = ta.Task(c)
            task_list.append(t)

        runner = ta.TestRunner(task_list)
        runner.start()

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
            'script': []}

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

