# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from framework.core import testcase
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_searchCountChart(self):
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()
        self.driver.find_id('statistics_amount').click()
        text1=self.driver.find_element_by_class_name('order_title').text
        self.driver.find_element_by_id('searchCountChart').click()
        self.driver.switch_to_alert()

        text2=self.driver.find_element_by_class_name('highcharts-title').text
        self.assertTrue(text1,text2)
        self.driver.find_element_by_link_text(u'关闭').click()
