# coding=utf-8
__author__ = 'guohai@live.com'

import os
import sys
import sqlite3
from util import excel


class TaskManager:

    file = ''
    mpath = sys.path[0] + os.sep + 'action' + os.sep+'singmodule'+os.sep
    conn = sqlite3.connect('c:\\test\\test.db')

    def __init__(self, file_name):
        self.file = file_name

    def save_data(self):
        pass

    def findCase(self, case_id):
        pass

    def findAllCase(self):
        pass

    def dispatchCase(self):
        pass

    #从case xls文件内读取用例存入到sqlite
    def read_case(self):
        tables = excel.Excel(self.mpath + 'action.xls').read_byname(0, 'Sheet1')
        pass