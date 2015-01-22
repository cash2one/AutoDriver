# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from framework.gui.views import auto_test_ui
from framework.gui.models import autotest_model
from framework.core import data
from framework.core import task as ta
from framework.util import fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

DB_PATH = '../../../result/'  # 存储测试结果数据的目录


class AutotestDialog(QDialog, auto_test_ui.Ui_Dialog):
    def __init__(self, task_data):
        QDialog.__init__(self)

        self.setupUi(self)

        self.connect(self, SIGNAL("finish_case"), self.show_test_result)
        self.connect(self, SIGNAL("over_all_case"), self.over_cases)
        self.tv_test_list.setFrameShape(QFrame.NoFrame)

        self.test_over = False

        self.result_data = ()
        self.taskModel = None

        print 'auto_test::',task_data
        self.start_task(task_data)

    def find_xls(self, task_data):
        path = task_data['path']
        idx = path.find('testcase') + len('testcase')
        opt = path[idx:0].replace(os.sep, '_')
        ini = fs.readConfig(PATH('../../config.ini'), 'task', opt)
        xls_name = fs.readConfig(PATH('../../manifest/%s' % ini), 'settings', 'test_case')
        return xls_name


    def start_task(self, task_data):
        db_folder = PATH(DB_PATH)
        if not os.path.exists(db_folder):
            os.mkdir(db_folder)

        db_path = os.path.join(db_folder, task_data['result'])
        print db_path
        if not os.path.exists(db_path):
            xls_file = ''#PATH('../../../resource/xls/%s' % self.find_xls(task_data['task']))
            #if os.path.exists(xls_file):
            gdata = data.generateData(xls_file, db_path)
            gdata.close()

        task_list = []
        for c in task_data['task']:
            t = ta.Task(c)
            task_list.append(t)

        runner = ta.TestRunner(task_list, db_path, self)
        runner.start()

    def show_test_result(self, data):
        d = data[3].replace('\r\n', '')

        new_data = (data[7], data[0], d)

        # d = {'row': data, 'script': []}
        if len(self.result_data) == 0:
            self.result_data += (new_data,)
            self.taskModel = autotest_model.QTableModel(self.result_data, self)
            self.tv_test_list.setModel(self.taskModel)
            self.tv_test_list.horizontalHeader().setStretchLastSection(True)
        else:
            self.taskModel.insertRows(new_data)
            self.taskModel.layoutChanged.emit()

    def over_cases(self):
        ret = QMessageBox.warning(self, u'测试完成',
                                  u"\n自动化脚本已经全部执行完成！",
                                  QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            self.test_over = True