# coding=utf-8
__author__ = 'guohai@live.com'

import sys
import os
import re
import unittest
from util import db
from core import test_runner
from util import excel
from core import HTMLTestRunner
from util import fileUtil
from core import service
from core import task
import time


def loadSuite():
    casePath = sys.path[0] + os.sep + 'testcase'
    #findCase(casePath)

    discover = unittest.defaultTestLoader.discover(casePath)
    suite = unittest.TestSuite()
    for test_suit in discover:
        for test_case in test_suit:
            suite.addTests(test_case)
    return suite

def testAllinCurrent():
    path = os.path.dirname(__file__)+os.sep+'testcase'
    files = os.listdir(path)

    # test = re.compile("test\.py{1}quot;",re.IGNORECASE)
    # files = filter(test.search, files)
    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    moduleNames = map(filenameToModuleName, files)
    print moduleNames

    modules = map(__import__, moduleNames)

    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))


# def runCases():
#     resultDir=sys.path[0] + os.sep + 'report' + os.sep+'abc.html'
#     fp = open(resultDir, 'wb')
#     dbm=db.DBManager()
#     runner=test_runner.NewTestRunner(
#         db=dbm,
#         stream=fp,
#         title=u'测试报告',
#         description=u'用例执行情况'
#     )
#     runner.run(loadSuite())

def loadmodule():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))+os.sep+'testcase'
    files = os.listdir(path)

    test = re.compile("^test.*?.py$", re.IGNORECASE)

    files = filter(test.search, files)

    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    moduleNames = map(filenameToModuleName, files)
    modules = map(__import__, moduleNames)

    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))

def main():
    # resultDir=sys.path[0] + os.sep + 'report' + os.sep+'abc.html'
    # fp = open(resultDir, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'测试报告',
    #     description=u'用例执行情况'
    # )
    #
    # s=loadSuite()
    # runner.run(s)


    #原生
    #unittest.TextTestRunner(verbosity=2).run(s)


    # cfg = sys.path[0] + os.sep + 'config' + os.sep
    # d=fileUtil.readConfig(cfg)
    #
    # tk=task.Task(False,d)
    # serv = service.Service(1,5,tk,loadSuite())
    # serv.start()

    print loadmodule()



if __name__ == "__main__":
    main()
