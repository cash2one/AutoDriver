# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os, sys, re
import unittest
import threading
import time
from framework.util import sqlite
import test_result
#from PyQt4 import QtCore
from framework.util import pyqt

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

RUNNING = 1
OVER_ALL = -1
FINISH = 0


class Task():
    def __init__(self, init_data):
        self.task_status = False
        print 'task core:',init_data
        self.datas = init_data
        self.path = self.datas['path']
        self.CASES = 'cases'
        self.STATUS = 'status'
        self.sys_path = ''

    def isRunning(self):
        # 是否运行中
        if self.datas[self.STATUS] == RUNNING:
            return True
        else:
            return False

    def isOver(self):
        # 是全部否完成
        if self.datas[self.STATUS] == OVER_ALL:
            return True
        else:
            return False

    def getPath(self):
        return self.datas['path']

    def getCases(self):
        left_cases = []
        for case_ in self.datas[self.CASES]:
            name = case_['name']
            loop = case_['loop']
            if loop > 0:
                left_cases.append(name.replace('.py', ''))
        return left_cases


    def getTestSuite(self):
        # 获取用例套件
        # path_cases = PATH('../../%s' % self.path)
        test = re.compile("^test.*?.py$", re.IGNORECASE)
        files = filter(test.search, os.listdir(self.path))

        filenameToModuleName = lambda f: os.path.splitext(f)[0]
        moduleNames = map(filenameToModuleName, files)

        # 继续过滤次数为0的case
        new_cases = []
        for f in moduleNames:
            if f in self.getCases():
                new_cases.append(f)

        modules = map(__import__, new_cases)  # moduleNames)
        load = unittest.defaultTestLoader.loadTestsFromModule
        return unittest.TestSuite(map(load, modules))

    def start(self):

        if r'\\' in self.path:
            self.sys_path = self.path.replace(r'\\', os.sep)
        else:
            self.sys_path = self.path.replace(r'/', os.sep)

        sys.path.append(self.sys_path)
        self.datas[self.STATUS] = RUNNING

    def finish(self):
        left_cases = 0  # 判断是否全部运行完毕
        cases = self.datas[self.CASES]
        for i in range(0, len(cases)):
            loop = cases[i]['loop']
            if loop > 0:
                loop -= 1
                #print 'tasks::::::',self.datas[self.CASES][i]
                #cases=[{'source': 'MyDemo\\demo', 'name': 'test_customer_allfinishOrder.py', 'loop': 0, 'desc': ''},
                #TODO: 未测试一个test类内的多个test方法的次数
                self.datas[self.CASES][i]['loop'] = loop  # 更新数据self.datas[self.CASES][ca] = num
                if loop > 0:  # 递减后的数量仍大于零
                    left_cases += 1

        if left_cases > 0:
            self.datas[self.STATUS] = FINISH
        else:
            self.datas[self.STATUS] = OVER_ALL

        sys.path.remove(self.sys_path)
        print '----------finish task------------'
        # print self.datas[self.CASES].values()


class TestRunner(threading.Thread):
    """
    主要负责监视Task的状态，当其为False时，说明一个Task运行已经结束，此时重新查找所有loop次数不为0的TestCase，
    再次启动下一次TestSuite的运行
    """

    def __init__(self, tasks, db_path='', ui=None):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.tasks = tasks
        self.task = None
        self.db_path = db_path
        self.dbm = None
        self.ui = ui

    # 取出一个未运行完毕的task
    def getTask(self):
        _task = None
        for t in self.tasks:
            if not t.isOver():
                _task = t
                break
        return _task

    def run(self):
        while not self.thread_stop:

            if self.getTask() == None:
                self.stop()
                #self.ui.emit(QtCore.SIGNAL("over_all_case"))
                pyqt.over_all_case(self.ui)
                return

            if self.task == None or not self.task.isRunning():
                self.task = self.getTask()

            self.task.start()

            product_info = None
            if len(self.db_path.strip()) == 0:
                self.dbm = None
            else:
                self.dbm = sqlite.DBManager(self.db_path)
            result = test_result.NewTestResult(self.dbm, product_info, self.ui)
            self.task.getTestSuite()(result)
            self.task.finish()

        time.sleep(5)

    def stop(self):
        if self.dbm != None:
            self.dbm.close_db()
        self.thread_stop = True