# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
import unittest
from framework.core import idriver_android


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        #self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_call_server(self):
        current_activity = self.driver.current_activity
        #点击进入使用
        self.driver.find_id('start_btn').click()
        #在附近司机界面点击联系客服
        self.driver.find_id('btn_call_server').click()
        self.driver.switch_to_alert()
        text_msg = self.driver.find_id('tvv_msg').text
        self.assertTrue(u'将拨打客服电话400-920-4358' in text_msg ,'msg')
        #点击拨打按钮
        self.driver.find_id('btn_right').click()