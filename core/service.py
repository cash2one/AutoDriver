# coding=utf-8
__author__ = 'Administrator'

import os
import threading
import time
from util import sqlite
import test_runner
import unittest
from util import fs


class Service(threading.Thread):
    """
    主要负责监视Task的状态，当其为False时，说明一个Task运行已经结束，此时重新查找所有loop次数不为0的TestCase，
    再次启动下一次TestSuite的运行
    """
    def __init__(self,task,tt=unittest.TestSuite()):
        threading.Thread.__init__(self)
        #self.thread_num = num
        #self.interval = interval
        self.thread_stop = False
        self.task = task
        self.tt = tt

    def run(self):
        while not self.thread_stop:
            #print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())
            if not self.task.getState():
                self.__startTestSuite(self.task,self.tt)#self.task.getTestSuite())

            time.sleep(5)
            #time.sleep(self.interval)

    def stop(self):
        self.thread_stop = True

    def __startTestSuite(self,task,suite):#suite要取消掉，用task.getTestSuite()
        db_path=fs.PATH('../config/autotest.db')
        dbm=sqlite.DBManager(db_path)
        runner=test_runner.NewTestRunner(
            db=dbm,
            task=task,
            title=u'测试报告',
            description=u'用例执行情况'
        )
        task.start()
        runner.run(suite)