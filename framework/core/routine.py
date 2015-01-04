# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import threading
import time
from framework.util import sqlite
import test_runner

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TaskAction(threading.Thread):
    """
    主要负责监视Task的状态，当其为False时，说明一个Task运行已经结束，此时重新查找所有loop次数不为0的TestCase，
    再次启动下一次TestSuite的运行
    """
    def __init__(self,task,db_path):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.task = task
        self.db_path = db_path

    def run(self):
        while not self.thread_stop:
            #print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())
            if not self.task.getState() and len(self.task.getTestData()) > 0:
                dbm=sqlite.DBManager(self.db_path)#integer
                runner=test_runner.TestRunner(
                    db=dbm,
                    task=self.task
                )

                self.task.start()
                runner.run(self.task.getTestSuite())
            else:
                self.stop()

            time.sleep(5)

    def stop(self):
        self.thread_stop = True

