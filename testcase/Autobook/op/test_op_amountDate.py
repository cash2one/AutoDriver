# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from framework.core import idriver_web
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_orderSource(self):
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('orderSource_amount').find_elements_by_tag_name('option')
        # for opt in opts:
        #     if opt.get_attribute('text')==u'按天':
        #         opt.click()
        # time.sleep(3)
        # startTime=self.driver.find_id('startTime_amount')
        # endTime=self.driver.find_id('endTime_amount')
        #
        # self.assertTrue(startTime.is_enabled()and endTime.is_enabled())

        for opt in opts:
            if opt.get_attribute('text')==u'按年':
                opt.click()
        time.sleep(3)
        startYear=self.driver.find_id('startYear')
        endYear=self.driver.find_id('endYear')

        self.assertTrue(startYear.is_enabled()and endYear.is_enabled())

