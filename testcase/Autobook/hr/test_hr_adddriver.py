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
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()

    # def test_driver_name(self,driver_name):
    #     self.testValue()
    #     self.driver.find_element_by_id('driverVo_name').send_keys(driver_name)


    def test_name0(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_name_tx=self.driver.find_element_by_id('driverVo_name_tip').text
        self.assertTrue(u'姓名不能为空.'in driverVo_name_tx)
        # driverVo_sfz_tx=self.driver.find_element_by_id('driverVo_card_tip').text
        # self.assertTrue(u'身份证号不能为空.'in driverVo_sfz_tx)


    def test_name1(self,driver_name):
        self.driver.find_element_by_id('driverVo_name').send_keys(driver_name)
        # self.driver.find_element_by_id('btn_add').click()

    def test_name_null(self):
        self.test_name1('')
    def test_name_long(self):
        self.test_name1('aaaaaaaaaaa')
    def test_name_num(self):
        self.test_name1('123')
    def test_name_specialCharacters(self):
        self.test_name1('#%%$#%')
    def test_name(self):
        self.test_name1(u'陈快乐')

    def test_sex0(self):
        self.test_name0()
        # self.driver.find_element_by_id('bth_add').click()
        driverVo_sex=self.driver.find_element_by_id('driverVo_sex_tip').text
        self.assertTrue(u'请选择性别.'in driverVo_sex)

    def test_sex1(self):
        sexs=self.driver.find_element_by_id('driverVo_sex').find_elements_by_tag_name('option')
        # time.sleep(1)
        for sex in sexs:
            if sex.get_attribute('value')=='0':
                sex.click()

    def test_sex2(self):
        sexs=self.driver.find_element_by_id('driverVo_sex').find_elements_by_tag_name('option')
        # time.sleep(1)
        for sex in sexs:
            if sex.get_attribute('value')=='1':
                sex.click()

    def test_marriage0(self):
        self.test_name0()
        # self.driver.find_element_by_id('bth_add').click()
        driverVo_marriage=self.driver.find_element_by_id('detailVo_marriage_tip').text
        self.assertTrue(u'请选择婚育.'in driverVo_marriage)


    def test_marriage1(self):
        marriages=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        # time.sleep(1)
        for marriage in marriages:
            if marriage.get_attribute('value')=='0':
                marriage.click()


    def test_marriage2(self):
        marriages=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        # time.sleep(1)
        for marriage in marriages:
            if marriage.get_attribute('value')=='1':
                marriage.click()










