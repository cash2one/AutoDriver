# coding=utf-8
__author__ = 'xuguanghua'

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

    def test_driver_Order(self):
        current_activity = self.driver.current_activity
        #点击附近司机列表
        self.driver.find_id('rb_maplist').click()

        driver_list = self.driver.find_tags('RelativeLayout')

        if driver_list:
            #若附近司机列表为真，则点击司机列表第一个,目前点击的第三个
            driver_list[0].click()
            self.driver.wait_switch(current_activity)
            #点击立即下单
            self.driver.find_id('driver_order').click()
            current_activity = self.driver.current_activity
            self.driver.wait_switch(current_activity)
            self.driver.switch_to_alert()
        else:
            pass
