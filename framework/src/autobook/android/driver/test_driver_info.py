# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        idriver.login_driver(self.driver)

    def tearDown(self):
        self.driver.switch_to_home()

    def test_order(self):
        idriver.changeWork(self.driver,True)

        isFound = False
        while not isFound:
            try:
                customer_names = self.driver.find_id('tv_customer_name')
                #for c in customer_names:
                if u'Guguohai' in customer_names.text:
                    isFound = True
            except NoSuchElementException:
                pass

        print 'tb_work_state'


        # self.driver.find_elements_by_id('cn.com.pathbook.idriver.driver:id/lv_order')
        # self.drivers.find_elements_by_accessibility_id('cn.com.pathbook.idriver.driver:id/lv_order')
        #
        # customer_name = device.findDynamicId('cn.com.pathbook.idriver.driver:id/tv_customer_name')
        #
        # self.driver.find_element_by_id('cn.com.pathbook.idriver.driver:id/iv_waiting')
        # self.driver.find

        #cn.com.pathbook.idriver.driver:id/tv_customer_name

        #cn.com.pathbook.idriver.driver:id/tb_work_state

