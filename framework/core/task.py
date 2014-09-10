# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os,sys,re
import unittest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append('testcase')

class Task():

    def __init__(self,device=None,test_num=1):
        self.device = device
        self.state = False
        self.test_num = test_num

    def getDevice(self):
        return self.device

    def getState(self):
        return self.state

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
        self.state = True

    def finish(self):
        self.state = False

        self.test_num = self.test_num -1


