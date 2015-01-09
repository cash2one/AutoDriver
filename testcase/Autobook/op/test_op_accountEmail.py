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


    def test_email1(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[2]/a').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_email').send_keys('<td>')
        self.driver.find_id('sure_create_account_btn').click()
        text=self.driver.find_id('operator_email_tip').text
        self.assertTrue(u'Email格式不正确' in text)

    def test_email2(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[2]/a').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_email').send_keys('dgfdgfdgdsdgfdgdgd')
        self.driver.find_id('sure_create_account_btn').click()
        text=self.driver.find_id('operator_email_tip').text
        self.assertTrue(u'Email格式不正确' in text)