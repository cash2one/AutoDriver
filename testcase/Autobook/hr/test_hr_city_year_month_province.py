# coding=utf-8
__author__ = 'lvfangying@pathbook.com.cn'

#hr_循环验证用户名错误登录测试

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
# from util.fileUtil import *
import os
from framework.core import testcase

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_city(self):

        self.driver.find_element_by_id('btn_add').click()
        driverVo_city_tx=self.driver.find_element_by_id('driverVo_city_tip').text
        self.assertTrue(u'请选择城市.'in driverVo_city_tx)

    def test_city1(self):

        citys=self.driver.find_element_by_id('driverVo_city').find_elements_by_tag_name('option')
        # time.sleep(1)
        for city in citys:
            if city.get_attribute('value')=='-99':
                city.click()

    def test_city2(self):

        citys=self.driver.find_element_by_id('driverVo_city').find_elements_by_tag_name('option')
        # time.sleep(1)
        for city in citys:
            if city.get_attribute('value')=='1':
                city.click()
#

    def test_year(self):

        self.driver.find_element_by_id('btn_add').click()
        driverVo_year_tx=self.driver.find_element_by_id('driverVo_year_tip').text
        self.assertTrue(u'请选择年份.'in driverVo_year_tx)

    def test_year1(self):

        years=self.driver.find_element_by_id('driverVo_year').find_elements_by_tag_name('option')
        # time.sleep(1)
        for year in years:
            if year.get_attribute('value')=='-99':
                year.click()

    def test_year2(self):

        years=self.driver.find_element_by_id('driverVo_year').find_elements_by_tag_name('option')
        # time.sleep(1)
        for year in years:
            if year.get_attribute('value')=='1995':
               year.click()

    def test_month(self):

        self.driver.find_element_by_id('btn_add').click()
        driverVo_month_tx=self.driver.find_element_by_id('driverVo_month_tip').text
        self.assertTrue(u'请选择月份.'in driverVo_month_tx)

    def test_month1(self):

        months=self.driver.find_element_by_id('driverVo_month').find_elements_by_tag_name('option')
        # time.sleep(1)
        for month in months:
            if month.get_attribute('value')=='-99':
                month.click()

    def test_month2(self):

        months=self.driver.find_element_by_id('driverVo_month').find_elements_by_tag_name('option')
        # time.sleep(1)
        for month in months:
            if month.get_attribute('value')=='1':
                month.click()