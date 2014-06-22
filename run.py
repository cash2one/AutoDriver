# coding=utf-8
__author__ = 'guohai@live.com'

import sys
import os
import unittest
import StringIO
from core import HTMLTestRunner
from util import excel
import ConfigParser

#读取测试配置文件
def readConf():
    dict={}
    conf = ConfigParser.ConfigParser()
    conf.read(sys.path[0] + os.sep+'config.cfg')
    #sections = conf.sections()
    options = conf.options('task')
    for opt in options:
        str_val = conf.get('task', opt)
        dict[opt]=str_val
    return dict

def loadSuite(paths):
    casePath = sys.path[0] + os.sep + 'testcase'
    discover = unittest.defaultTestLoader.discover(casePath)
    suite = unittest.TestSuite()
    for test_suit in discover:
        for test_case in test_suit:
            suite.addTests(test_case)
    return suite

def main():
    #print readConf().keys()
    resultDir=sys.path[0] + os.sep + 'report' + os.sep+'abc.html'
    fp = open(resultDir, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况'
    )

    s=loadSuite()
    runner.run(s)


if __name__ == "__main__":
    main()
