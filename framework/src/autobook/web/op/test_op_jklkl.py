# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
import os
import unittest
from framework.core import idriver_web

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.get('http://192.168.3.31/op/core/login/login.html')

    def tearDown(self):
        #返回首页
        self.driver.close()
        pass

    def test_my_info(self):
        self.driver.find_id('username').clear()
        self.driver.find_id('username').send_keys('zc01')
