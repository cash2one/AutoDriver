# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()
    #指定司机下单
    def test_driver_Order(self):

        current_activity = self.driver.current_activity
        # 点击附近司机列表
        self.driver.find_id('rb_map_list').click()
        self.driver.wait_loading()

        nearbyrivers = []
        try:
            nearbyrivers = self.driver.find_ids('nearbyriver')
        except self.driver.NoSuchElementException:
            pass

        self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')

        driver_exist = False

        for d in nearbyrivers:
            d_name = d.find_element_by_id(self.driver.pkg+'big_drivername').text
            self.driver.swipe(0,0,0,100,0.8)

            print d_name
            if u'康小薇哈' in d_name:
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


