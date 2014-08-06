# coding=utf-8
__author__ = 'Administrator'
import unittest
from time import sleep
from framework.core import gvar,device


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = gvar.driver

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)


    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity

        self.driver.find_element_by_name(u'24小时服务站').click()

        #有loading的webview页面，需要后期考虑
        sleep(10)
        self.driver.find_element_by_name(u'详情').click()
