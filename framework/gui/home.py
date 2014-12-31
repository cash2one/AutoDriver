# coding=utf-8
__author__ = 'Administrator'

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.gui.ui import home_ui
from framework.gui.models import table_model
import dlg_task

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeForm(QWidget, home_ui.Ui_Form):
    '''
    首页
    '''

    def __init__(self):
        super(HomeForm, self).__init__()

        self.setupUi(self)

        self.dlgTask=None
        # self.table_task.setHorizontalHeaderLabels([u'编号', u'任务名称', u'任务状态', u'任务类型',
        #                                            u'优先级', u'执行人', u'创建人', u'创建时间'])
        #
        # self.table_task.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.table_task.setEditTriggers(QTableWidget.NoEditTriggers)
        # self.table_task.setAlternatingRowColors(True)
        #
        # # table_rows = self.table_task.rowCount()
        # # table_cols = self.table_task.columnCount()
        # self.table_task.setColumnWidth(1, 300)
        #
        # for ts in range(0, len(self.task_data)):
        #     infos = self.task_data[ts]['info']
        #     for t in range(0, len(infos)):
        #         newItem = QTableWidgetItem(infos[t])
        #         self.table_task.setItem(ts, t, newItem)

        header=(u'编号', u'任务名称', u'任务状态', u'任务类型', u'优先级', u'执行人', u'创建人', u'创建时间')
        task_data= [(u'001', u'接口测试', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-22'),
                      (u'001', u'接口测试', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-22'),
                      (u'001', u'接口测试', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-22'),
                      (u'001', u'接口测试', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-22'),
                      (u'001', u'接口测试', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-22')]

        # self.tasks = ({'info': (u'001', u'接口测试', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-22'), 'autos': []},
        #               {'info': (u'002', u'app平台测试', u'未开始', u'自动化', u'高', u'顾国海', u'顾国海', u'2015-02-23'), 'autos': []})
        self.tvModel = table_model.MyTableModel(header,task_data, self)
        # tablemodel.setHorizontalHeaderLabels([u'编号', u'任务名称', u'任务状态', u'任务类型',
        # u'优先级', u'执行人', u'创建人', u'创建时间'])
        # tablemodel.setHeaderData(0, Qt.Horizontal, QVariant("ID"))
        # tablemodel.setHeaderData(1, Qt.Horizontal, QVariant("File Order"))

        self.tv_task.setModel(self.tvModel)

        self.tv_task.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_task.setColumnWidth(1, 300)
        self.tv_task.setAlternatingRowColors(True)
        self.tv_task.horizontalHeader().setStretchLastSection(True)
        self.connect(self.tv_task, SIGNAL("doubleClicked(const QModelIndex&)"),self.show_current_task)

    def ddd(self):
        idx= self.tv_task.currentIndex()
        if idx.isValid():
            print self.tvModel.rowContent(idx.row())

        #self.table_task.show()

    def delRow(self, data):
        self.table_task.removeRow()

    def insertRow(self, data):
        self.table_task.insertRow()


    def show_current_task(self):
        idx= self.tv_task.currentIndex()
        if idx.isValid():
            _data= self.tvModel.rowContent(idx.row())

            #current_row = self.frm_home.table_task.currentRow()
            #row_data = self.tasks[current_row]['info']
            if self.dlgTask == None:
                self.dlgTask = dlg_task.TaskDialog()

            self.dlgTask.txt_TaskName.setText(_data[1])
            self.dlgTask.txt_Creator.setText(_data[5])
            self.dlgTask.exec_()