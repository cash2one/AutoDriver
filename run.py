# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os,sys
import time,re
from framework.core import HTMLTestRunner,gvar,device
import unittest


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append('testcase')

def getTestSuite():
    path = PATH('./testcase/')

    test = re.compile("^test.*?.py$", re.IGNORECASE)
    files = filter(test.search, os.listdir(path))

    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    moduleNames = map(filenameToModuleName, files)
    print moduleNames

    modules = map(__import__, moduleNames)
    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))


def main():
    t= time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    resultDir = PATH('./report%s.html') % t
    fp = open(resultDir, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况'
    )

    #启动apk，并等待
    gvar.driver = device.android()
    time.sleep(30)

    runner.run(getTestSuite())


if __name__ == "__main__":
    main()

