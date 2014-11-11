# coding=utf-8
__author__ = 'xuguanghua'

import time
import unittest
from framework.core import idriver_android
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_driver_Order(self):

        current_activity = self.driver.current_activity
        # 点击附近司机列表
        self.driver.find_id('rb_maplist').click()
        self.driver.wait_loading()

        #若附近司机列表为真，则点击司机列表第一个,目前点击的第三个
        nearbyrivers = []
        try:
            nearbyrivers = self.driver.find_ids('nearbyriver')
        except NoSuchElementException:
            pass

        self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')

        driver_exist = False

        for d in nearbyrivers:
            d_name = d.find_element_by_id(self.driver.pkg+'big_drivername').text
            self.driver.swipe(0,0,0,100,0.8)

            print d_name
            if u'蒋芷文' in d_name:
                driver_exist = True
                d.click()
                self.driver.wait_switch('.MainActivity')

                # 点击立即下单
                self.driver.find_id('driver_order').click()
                self.driver.wait_loading()

                tv_wait = self.driver.find_id('tv_wait').text
                self.assertTrue(int(tv_wait) > 0, 'fail')

                self.driver.countdown()

                break

        self.assertTrue(driver_exist, u'没有找到指定司机')

