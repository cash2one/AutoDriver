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

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AutotestDialog(QDialog, auto_test_ui.Ui_Dialog):
    def __init__(self, scripts):
        QDialog.__init__(self)

        self.setupUi(self)

        self.connect(self, SIGNAL("finish_case"), self.show_test_result)
        self.connect(self, SIGNAL("over_all_case"), self.over_cases)
        self.tv_test_list.setFrameShape(QFrame.NoFrame)

        self.test_over = False

        self.result_data = ()
        self.taskModel = None

        print scripts
        self.start_task(scripts)

    def start_task(self, scripts):
        time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        report_db = 'report' + time_str + '.db'
        db_path = PATH('../../../%s' % report_db)

        gdata = data.generateData(PATH('../../../resource/xls/'), db_path)
        gdata.close()

        task_list = []
        for c in scripts:
            t = ta.Task(c)
            task_list.append(t)

        runner = ta.TestRunner(task_list, db_path, self)
        runner.start()

    def show_test_result(self, data):
        new_data = (data[7], data[0], data[3])

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