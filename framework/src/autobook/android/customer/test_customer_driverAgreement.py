
# coding=utf-8

__author__ = 'wangsahnshan@126.com'
#用户登录，查看代驾协议

import time
import unittest
from framework.core import idriver_android
from selenium.common.exceptions import NoSuchElementException


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()


    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_drive_Agreement(self):

       current_activity = self.driver.current_activity
       #点击进入使用
       # self.driver.find_id('start_btn').click()
       # self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #点击代驾协议
       self.driver.find_ids('person_item')[3].click()


       text=self.driver.find_id('tv_title_text').text
       print text
       self.assertTrue(u'代驾协议' in text,'msg')

       #点击左上角返回按钮
       self.driver.find_id('button_title_back').click()
