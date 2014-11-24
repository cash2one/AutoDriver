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

     #司机信息都为空
    def test_allEmpty(self):
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        self.driver.find_id('send_new_psd').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'司机工号不能为空' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity

     #司机工号不存在
    def test_(self):
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        self.driver.find_id('driver_no')
        driver_txt = self.driver.find_id('driver_no').text
        print driver_txt
        driver_no=self.driver.sql('SELECT no FROM autobook.t_driver',1)
        print driver_no
        self.assertTrue(driver_no== driver_txt)






# driver_no
# driver_phone
#
# send_new_psd