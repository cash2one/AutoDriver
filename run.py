# coding=utf-8
__author__ = 'guohai@live.com'

import sys
import os
import unittest
from util import db
from core import test_runner
from util import excel


def loadSuite():
    casePath = sys.path[0] + os.sep + 'testcase'
    #findCase(casePath)

    discover = unittest.defaultTestLoader.discover(casePath)
    suite = unittest.TestSuite()
    for test_suit in discover:
        for test_case in test_suit:
            suite.addTests(test_case)

    return suite

def main():
    resultDir=sys.path[0] + os.sep + 'report' + os.sep+'abc.html'
    fp = open(resultDir, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'测试报告',
    #     description=u'用例执行情况'
    # )

    #s=loadSuite()
    #runner.run(s)

    #原生
    #unittest.TextTestRunner(verbosity=2).run(s)
    #runner.Runner(verbosity=2).run(s)

    dbm=db.DBManager()
    runner=test_runner.NewTestRunner(
        db=dbm,
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况'
    )
    runner.run(loadSuite())


if __name__ == "__main__":
    main()
