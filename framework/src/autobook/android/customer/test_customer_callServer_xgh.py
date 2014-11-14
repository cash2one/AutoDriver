# coding=utf-8
__author__ = 'xuguanghua'

import time
import unittest
from framework.core import idriver_android


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer()
        #self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_call_server(self):
        current_activity = self.driver.current_activity
        #在附近司机界面点击联系客服
        self.driver.find_id('btn_callserver').click()
        self.driver.switch_to_alert()
        text_msg = self.driver.find_id('tvv_msg').text
        self.assertTrue(u'将拨打客服电话400-800-8888' in text_msg ,'msg')
        #点击拨打按钮
        self.driver.find_id('btn_right').click()