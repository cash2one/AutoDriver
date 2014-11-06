# coding=utf-8
__author__ = 'xuguanghua'

import time
import unittest
from framework.core import device,idriver
from selenium.common.exceptions import NoSuchElementException

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
        self.driver.wait_loading()
        #nearby_list = self.driver.find_id('nearbyriver')

        #if nearby_list:
            #若附近司机列表为真，则点击司机列表第一个,目前点击的第三个

        try:
           driverName_list = self.driver.find_elements_by_id('nearbyriver')
        except NoSuchElementException:
            pass

        print driverName_list

        if len(driverName_list)>0:
            for i in range(0,len(driverName_list)):
                if driverName_list[i].find_element_by_id(self.package+'big_drivername').text == u'司马小二啊哈':
                    print i
                    driverName_list[i].click()
                    self.driver.wait_switch()
                    #点击立即下单
                    self.driver.find_id('driver_order').click()
                    self.driver.wait_loading()

                    tv_wait = self.driver.find_id('tv_wait').text
                    self.assertTrue(int(tv_wait)>0,'fail')
        #else:
        #    print "附近没有司机，请拨打客服电话"
