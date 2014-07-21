# coding=utf-8
__author__ = 'guohai@live.com'

import sys
import os
import re
import unittest
from util import fs
from util import sqlite
from core import test_runner
from util import xls
#from core import HTMLTestRunner
from core import service
from core import task
import time
from util import jsons
from util import inf
from testcase import suites



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

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
    # files = os.listdir(path)

    f=fs.findCase(path)

    # test = re.compile("test\.py{1}quot;",re.IGNORECASE)
    # files = filter(test.search, files)
    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    moduleNames = map(filenameToModuleName, f)
    #print moduleNames

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

    # dbm=db.DBManager()
    # modules = dbm.fetchall('select * from module where id>3')
    #
    #
    # for m in modules:
    #     for i in range(len(m)):
    #         print m[i]


    #原生
    #unittest.TextTestRunner(verbosity=2).run(s)

    # PATH = lambda p: os.path.abspath(
    #     os.path.join(os.path.dirname(__file__), p)
    # )
    #
    # cfg = sys.path[0] + os.sep + 'config' + os.sep
    # d=files.readConfig(cfg)
    #
    # tk=task.Task(False,d)
    # serv = service.Service(tk,PATH('config/autotest.db'),loadSuite())
    # serv.start()

    #ss=load_tests(loader)
    # a='{"weatherinfo":{"city":"上海","cityid":"101020100","temp":"29","WD":"西南风","WS":"1级","SD":"56%","WSE":"1","time":"12:45","isRadar":"1","Radar":"JC_RADAR_AZ9210_JB"}}'
    # jn = parseJson.fromStr(a)
    # print parseJson.find_value_by_key(jn, 'cityid')

    #print test_suite.loadmodule()
    print suites.regressionTest()


def load_tests(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests



if __name__ == "__main__":
    main()
