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

        #司机不存在
    def test_inexistence(self):
        self.driver.find_id('et_username').clear()
        self.driver.find_id('et_username').send_keys('123abc')
        self.driver.find_id('et_password').clear()
        self.driver.find_id('et_password').send_keys('123456')
        self.driver.find_id('bt_login').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'不存在司机工号为:123Abc的用户或数据库异常.' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity

        #密码错误
    def test_password_error(self):
        self.driver.find_id('et_username').clear()
        self.driver.find_id('et_username').send_keys('140015')
        self.driver.find_id('et_password').clear()
        self.driver.find_id('et_password').send_keys('1')
        self.driver.find_id('bt_login').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'密码错误' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity

        #登录成功
    def test_login(self):
        self.driver.find_id('et_username').clear()
        self.driver.find_id('et_username').send_keys('140015')
        self.driver.find_id('et_password').clear()
        self.driver.find_id('et_password').send_keys('123456')
        self.driver.find_id('bt_login').click()
        current_activity = self.driver.current_activity
        #判断是否正确跳转至对应的界面
        print(self.driver.current_activity)
        # self.assertEqual('.LoginActivity',self.driver.current_activity)








