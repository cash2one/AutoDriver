# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import datetime
from framework.core import testcase
import unittest
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        # self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()


    def test_newpage(self):
        #判断是否跳转至对应的界面
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        self.driver.find_id('driver_no').send_keys('140014')
        self.driver.find_id('driver_phone').send_keys('13122302705')
        self.driver.find_id('send_new_psd').click()
        current_activity = self.driver.current_activity
        print(self.driver.current_activity)
        newno=self.driver.find_id('driver_no').text
        newphone=self.driver.find_id('driver_phone').text
        print newno,newphone

    