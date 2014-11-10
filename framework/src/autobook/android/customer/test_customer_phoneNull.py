# coding=utf-8

__author__ = 'wangsahnshan'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.customer')
        idriver.login_customer(self.driver)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       #点击用户中心
       self.driver.find_id('btn_personalcenter').click()
       #点击我的信息
       #self.driver.find_id('personal_name').click()
       #点击我的信息
       self.driver.find_ids('personal_name')[0].click()
       #在填写手机号界面点击下一步
       self.driver.find_id('next_step').click()
       self.driver.switch_to_alert()
       text=self.driver.find_id('tv_msg').text
       print text
       self.assertTrue(u'请填写手机号！' in text,'msg')
