# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()
    #一键下单
    def test_rb_Order(self):

        current_activity = self.driver.current_activity
        #点击一键下单，进入一键下单界面
        self.driver.find_id('rb_order').click()
        #点击立即下单
        self.driver.find_id('bt_order').click()
        self.driver.wait_loading()

        tv_wait = self.driver.find_id('tv_wait').text
        self.assertTrue(int(tv_wait)>0,'fail')







