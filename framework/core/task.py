# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os,sys,re
import unittest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append('testcase')

class Task():

    __state = False
    __testDatas=[]
    __polling = False
    task_id = 0

    def __init__(self,device=None,state=False,test_num=1):
        self.device = device
        self.__state = state
        self.test_num = test_num

    def getDevice(self):
        return self.device

    def getState(self):
        return self.__state

    def getTestNum(self):
        return self.test_num

    def getTestSuite(self):
        path = PATH('../../testcase/')

        test = re.compile("^test.*?.py$", re.IGNORECASE)
        files = filter(test.search, os.listdir(path))

        filenameToModuleName = lambda f: os.path.splitext(f)[0]
        moduleNames = map(filenameToModuleName, files)

        modules = map(__import__, moduleNames)
        load = unittest.defaultTestLoader.loadTestsFromModule
        return unittest.TestSuite(map(load, modules))

    def start(self):
        self.__state = True

    def finish(self):
        self.__state = False

        self.test_num = self.test_num -1


