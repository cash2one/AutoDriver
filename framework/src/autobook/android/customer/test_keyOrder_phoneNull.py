# coding=utf-8

__author__ = 'wangsahnshan@126.com'
#用户登录，联系电话为空（若不为空，删除电话号码）

import time

import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()


    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):


       self.driver.wait_loading()
       #点击一键下单按钮跳转到一键下单界面
       self.driver.find_id('rb_order').click()

       #删除联系电话
       self.driver.find_id('tv_phone').click()
       self.driver.clear_text('tv_phone')
       # text=self.driver.find_id('tv_phone').text
       # print text
       # for i in range(0,len(text)):
       #     self.driver.keyevent(67)


       # #点击立即下单
       # self.driver.find_id('bt_order').click()
       # # 弹出提示框请填写手机号
       # self.driver.switch_to_alert()
       # text=self.driver.find_id('tv_msg').text
       # print text
       # self.assertTrue(u'请填写手机号！' in text,'msg')
