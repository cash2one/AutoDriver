# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os, sys, re
import unittest
import threading
import time
from framework.util import const, sqlite
import test_runner
import threading
import time
from framework.util import sqlite
import test_runner_temp,test_result_temp

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

RUNNING = 1
OVER_ALL = -1
FINISH = 0


class Task():
    def __init__(self, init_data):
        self.task_status = False
        self.datas = init_data
        self.path = self.datas['path']
        self.CASES = 'cases'
        self.STATUS = 'status'

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
        for a in self.datas[self.CASES]:
            if self.datas[self.CASES][a] > 0:
                left_cases.append(a)
        return left_cases


    def getTestSuite(self):
        #获取用例套件
        path_cases = PATH('../../%s' % self.path)
        test = re.compile("^test.*?.py$", re.IGNORECASE)
        files = filter(test.search, os.listdir(path_cases))

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
        sys.path.append(self.path.replace('/', os.sep))
        self.datas[self.STATUS] = RUNNING

    def finish(self):
        left_cases = 0  # 判断是否全部运行完毕
        for ca in self.datas[self.CASES]:
            num = self.datas[self.CASES][ca]
            if num > 0:
                num -= 1
                self.datas[self.CASES][ca] = num
                if num > 0:#递减后的数量仍大于零
                    left_cases += 1

        if left_cases > 0:
            self.datas[self.STATUS] = FINISH
        else:
            self.datas[self.STATUS] = OVER_ALL

        sys.path.remove(self.path.replace('/', os.sep))
        print '----------------------'
        # print self.datas[self.CASES].values()



class TestRunner(threading.Thread):
    """
    主要负责监视Task的状态，当其为False时，说明一个Task运行已经结束，此时重新查找所有loop次数不为0的TestCase，
    再次启动下一次TestSuite的运行
    """

    def __init__(self, tasks):  # ,db_path):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.tasks = tasks
        self.task = None
        # self.db_path = db_path

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
                return

            if self.task == None or not self.task.isRunning():
                self.task = self.getTask()

            # runner = test_runner_temp.TestRunner(
            #     # db=dbm,
            #     task=self.task
            # )
            #
            # self.task.start()
            # runner.run(self.task.getTestSuite())
            self.task.start()
            result = test_result_temp.NewTestResult()
            self.task.getTestSuite()(result)
            self.task.finish()

        time.sleep(5)

    def stop(self):
        self.thread_stop = True