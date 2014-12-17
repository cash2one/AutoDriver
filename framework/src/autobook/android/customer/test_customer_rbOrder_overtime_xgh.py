# coding=utf-8
__author__ = 'guanghua_2011@126.comjhhhh'

import time
import unittest
from framework.core import idriver_android


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_rb_selectDriver(self):
        current_activity = self.driver.current_activity
        #点击一键下单，进入一键下单界面
        self.driver.find_id('rb_order').click()
        #点击立即下单
        self.driver.find_id('bt_order').click()
        self.driver.wait_loading()

        tv_wait = self.driver.find_id('tv_wait').text
        self.assertTrue(int(tv_wait)>0,'fail')


        self.driver.switch_to_alert()

        # tv_order_service = self.driver.find_id('select').text
        # if u'轮单失败' in tv_order_service :
        #点击重新选择司机下单
        self.driver.find_id('select_driver').click()
        self.driver.wait_loading()
        # else :
        #     pass
