__author__ = 'wangshanshan'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from framework.core import *

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver=web.firefox(alias.ir)
        self.driver.login()


    def tearDown(self):
        pass

    def test_list(self):
        print self.driver.find_element_by_id('welcome').text


    def test_next(self):
        self.driver.find_element_by_id('myNes').click()
        self.driver.implicitly_wait(30)
        print self.driver.find_element_by_id('realName').text







