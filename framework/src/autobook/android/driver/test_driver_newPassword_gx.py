# coding=utf-8
__author__ = 'gaoxu'

import datetime
from framework.core import idriver_android
import unittest
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.driver()
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
        self.assertEqual('.ForgetPsdActivity',self.driver.current_activity)
