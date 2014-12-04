# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import device_bak


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device_bak.android()
        print self.driver

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity

        self.driver.find_elements_by_class_name('android.widget.Button')[0].click()

        #对于动态生成的View，比如用户下单，用以下语句
        isCurrent = False

        while not isCurrent:
            isCurrent = device_bak.isCurrentActivity('.EManualActivity')
        else:
            print 'find success!!'

