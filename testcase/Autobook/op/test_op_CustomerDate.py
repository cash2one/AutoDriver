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

    def test_orderDate(self):
        '''
        切换时间粒度，显示对应的下拉框
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()

        opts=self.driver.find_id('dateType').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'按天':
                opt.click()
        time.sleep(3)
        startTime=self.driver.find_id('startTime')
        endTime=self.driver.find_id('endTime')

        self.assertTrue(startTime.is_enabled()and endTime.is_enabled())

        for opt in opts:
            if opt.get_attribute('text')==u'按年':
                opt.click()
        time.sleep(3)
        startYear=self.driver.find_id('startYear')
        endYear=self.driver.find_id('endYear')

        self.assertTrue(startYear.is_enabled()and endYear.is_enabled())

        for opt in opts:
            if opt.get_attribute('text')==u'按月':
                opt.click()
        time.sleep(3)
        startMonth=self.driver.find_id('startMonth')
        endMonth=self.driver.find_id('endMonth')
        self.assertTrue(startMonth.is_enabled()and endMonth.is_enabled())

    def test_dateControl(self):
        '''
        结束时间小于开始时间，系统给出错误提示
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()

        js = '$(\'input[id=startTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime').clear()
        self.driver.find_element_by_id('startTime').send_keys('2015-01-06')
        #选择开始时间
        js = '$(\'input[id=endTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime').clear()
        self.driver.find_element_by_id('endTime').send_keys('2015-01-01')
        self.driver.find_id('statistics').click()
        #选择结束时间
        time.sleep(3)
        text=self.driver.switch_to_alert().text
        self.assertEqual(text,u'开始时间不能大于结束时间，请重新选择！')
        self.driver.switch_to_alert().accept()
        print(text)

    def test_dateControl1(self):
        '''
        结束时间小于开始时间，系统给出错误提示
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()

        js = '$(\'input[id=startTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime').clear()
        self.driver.find_element_by_id('startTime').send_keys('2014-11-06')
        #选择开始时间
        js = '$(\'input[id=endTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime').clear()
        self.driver.find_element_by_id('endTime').send_keys('2015-01-01')
        self.driver.find_id('statistics').click()
        #选择结束时间
        time.sleep(3)
        text=self.driver.switch_to_alert().text
        self.assertEqual(text,u'按天统计，只统计30天内的数据，请重新选择！')
        self.driver.switch_to_alert().accept()
        print(text)

