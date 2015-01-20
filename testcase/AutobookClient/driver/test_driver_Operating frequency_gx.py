# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
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
        # self.assertEqual('.ForgetPsdActivity',self.driver.current_activity)
        self.driver.back()
        #判断是否跳转至对应的界面
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        #再次返回输入获取新密码
        self.driver.find_id('driver_no').send_keys('140014')
        self.driver.find_id('driver_phone').send_keys('13122302705')
        self.driver.find_id('send_new_psd').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'请求过于频繁' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity





