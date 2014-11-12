# coding=utf-8

__author__ = 'wangsahnshan'

import time
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer()
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       #点击用户中心
       self.driver.find_id('btn_personalcenter').click()
       #查看如何收费
       self.driver.find_ids('personal_name')[2].click()

       text=self.driver.find_id('tv_title_text').text
       print text
       self.assertTrue(u'如何收费' in text,'msg')
