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



    #司机信息都为空
    def test_no_null(self):
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        #判断是否正确跳转至对应的界面
        print(self.driver.current_activity)
        # self.assertEqual('.ForgetPsdActivity',self.driver.current_activity)
        self.driver.find_id('send_new_psd').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'司机工号不能为空' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity


         #司机手机号码为空
    def test_phone_null(self):
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        #判断是否正确跳转至对应的界面
        print(self.driver.current_activity)
        # self.assertEqual('.ForgetPsdActivity',self.driver.current_activity)
        self.driver.find_id('driver_no').clear()
        self.driver.find_id('driver_no').send_keys('140014')
        self.driver.find_id('send_new_psd').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'司机手机号不能为空' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity


    #司机工号错误
    def test_no_error(self):
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        #判断是否正确跳转至对应的界面
        print(self.driver.current_activity)
        # self.assertEqual('.ForgetPsdActivity',self.driver.current_activity)
        self.driver.find_id('driver_no').clear()
        self.driver.find_id('driver_no').send_keys('123abc')
        self.driver.find_id(' driver_phone').send_keys('13122302222')
        self.driver.find_id('send_new_psd').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'不存在司机工号为:123abc的用户或数据库异常.' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity


        #司机手机号码格式错误
    def test_phone_error(self):
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        #判断是否正确跳转至对应的界面
        print(self.driver.current_activity)
        # self.assertEqual('.ForgetPsdActivity',self.driver.current_activity)
        self.driver.find_id('driver_no').clear()
        self.driver.find_id('driver_no').send_keys('140015')
        self.driver.find_id(' driver_phone').send_keys('1234')
        self.driver.find_id('send_new_psd').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'手机号码格式不正确' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity


      #司机手机号码格式错误
    def test_phone_mismatches(self):
        self.driver.find_id('login_forget').click()
        current_activity = self.driver.current_activity
        #判断是否正确跳转至对应的界面
        print(self.driver.current_activity)
        # self.assertEqual('.ForgetPsdActivity',self.driver.current_activity)
        self.driver.find_id('driver_no').clear()
        self.driver.find_id('driver_no').send_keys('140015')
        self.driver.find_id(' driver_phone').send_keys('13100000000')
        self.driver.find_id('send_new_psd').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'手机号错误' in txt)
        self.driver.find_id('btn_confirm').click()
        current_activity = self.driver.current_activity


