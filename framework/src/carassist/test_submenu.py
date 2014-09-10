# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import the,device


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity

        self.driver.find_elements_by_class_name('android.widget.Button')[0].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('android.widget.Button')[0].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('android.widget.Button')[2].click()

