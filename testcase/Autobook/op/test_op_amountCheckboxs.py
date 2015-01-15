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

    def test_orderSource(self):
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('orderSource_amount').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'全部')
        #订单来源默认显示全部
        tuple=(u'全部',u'平台下单',u'客户下单',u'微信下单')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break
        time.sleep(2)
        self.assertTrue(isExist,'false')
        #查看订单来源下拉框中的选项


    def test_orderType(self):
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('orderType_amount').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'全部')
        #订单类型默认显示全部
        tuple=(u'全部',u'指定下单',u'周边下单')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break
        time.sleep(2)
        self.assertTrue(isExist,'false')
        #查看订单类型下拉框中的选项


    def test_dateType(self):
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('dateType_amount').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'按天')
        #时间粒度默认显示全部
        tuple=(u'按天',u'按年',u'按月')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break
        time.sleep(2)
        self.assertTrue(isExist,'false')
        #查看时间粒度下拉框中的选项



