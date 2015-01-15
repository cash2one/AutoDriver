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

    def test_mobileNull(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_name').send_keys(u'lishan1')
        self.driver.find_id('operator_realName').send_keys(u'李三1')
        self.driver.find_id('sure_create_account_btn').click()
        mobile=self.driver.find_id('operator_mobile_tip').text
        self.assertTrue(u'手机号码不能为空' in mobile)

    def test_mobileError(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_name').send_keys(u'lishan1')
        self.driver.find_id('operator_realName').send_keys(u'李三1')
        self.driver.find_id('operator_mobile').send_keys(u'1815536')
        self.driver.find_id('sure_create_account_btn').click()
        mobile=self.driver.find_id('operator_mobile_tip').text
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.'in mobile)

        self.driver.find_id('operator_mobile').clear()
        self.driver.find_id('operator_mobile').send_keys(u'gjkfsjgkljsssss')
        self.driver.find_id('sure_create_account_btn').click()
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.'in mobile)

        self.driver.find_id('operator_mobile').clear()
        self.driver.find_id('operator_mobile').send_keys('<td>')
        self.driver.find_id('sure_create_account_btn').click()
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.'in mobile)