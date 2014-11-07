# coding=utf-8
__author__ = 'xuguanghua'

import time
import unittest
from framework.core import device,idriver
from selenium.common.exceptions import NoSuchElementException

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.customer',idriver.Action)
        idriver.login_customer(self.driver)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_driver_Order(self):
        current_activity = self.driver.current_activity
        #点击附近司机列表
        self.driver.find_id('rb_maplist').click()
        self.driver.wait_loading()
        #nearby_list = self.driver.find_id('nearbyriver')

        #if nearby_list:
            #若附近司机列表为真，则点击司机列表第一个,目前点击的第三个
        driverName_list = []
        try:
            driverName_list = self.driver.find_elements_by_id(self.driver.package + 'nearbyriver')
        except NoSuchElementException:
            pass
        print driverName_list
        self.assertTrue(len(driverName_list) > 0, u'附近没有司机')

        driver_exist = False
        for i in range(0, len(driverName_list)):
            if driverName_list[i].find_element_by_id(self.driver.package + 'big_drivername').text == u'司马小二啊哈':
                driver_exist = True
                driverName_list[i].click()
                self.driver.wait_switch('.MainActivity')
                # 点击立即下单
                self.driver.find_id('driver_order').click()
                self.driver.wait_loading()

                tv_wait = self.driver.find_id('tv_wait').text
                self.assertTrue(int(tv_wait) > 0, 'fail')

                #等待订单倒计时结束
                self.driver.extra().order_countdown()
                idriver.order_countdown(self.driver)

                break
        self.assertTrue(driver_exist, u'没有找到指定司机')

