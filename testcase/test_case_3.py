__author__ = 'Administrator'
# coding=utf-8

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.ff.implicitly_wait(10) #设置网页打开超时时间

    def tearDown(self):
        self.ff.close()

    def test_qq(self):
        self.ff.get("http://www.qq.com")
        try:
            self.ff.find_element_by_id('newsMoreBtn')
        except NoSuchElementException:
            assert 0, "can't find qq"


if __name__ =='__main__':
    unittest.main()