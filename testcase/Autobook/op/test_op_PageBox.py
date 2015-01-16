# coding=utf-8
__author__ = 'xhl'


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
    #查询分页
    def test_logall(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        ActionChains(self.driver).move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        time.sleep(1)
        opts=self.driver.find_element_by_class_name('ui-pg-selbox').find_elements_by_tag_name('option').click()

