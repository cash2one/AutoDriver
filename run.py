# coding=utf-8
__author__ = 'guohai@live.com'

import os
import time
from framework.core import HTMLTestRunner
import unittest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def getSuite():
    casePath = PATH('./testcase/')
    discover = unittest.defaultTestLoader.discover(casePath)
    suite = unittest.TestSuite()
    for test_suit in discover:
        for test_case in test_suit:
            suite.addTests(test_case)
    return suite


def main():
    t= time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    resultDir = PATH('./report%s.html') % t
    fp = open(resultDir, 'wb')
    suite = getSuite()
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况'
    )
    runner.run(suite)



if __name__ == "__main__":
    main()
