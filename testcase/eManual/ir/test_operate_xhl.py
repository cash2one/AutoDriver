# coding=utf-8
__author__ = 'xhl'

#hr_循环添加司机多选框测试lll
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from framework.core import idriver_web
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login('role_operation')

    def tearDown(self):
        #返回首页
        self.driver.close()




    def test_my_batch(self):
        self.driver.find_element_by_id('uploader').send_keys(u'你好啊')
        self.driver.find_element_by_id('query').click()





