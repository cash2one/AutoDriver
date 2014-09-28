__author__ = 'zhangchun'
# coding=utf-8

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from util.fileUtil import *
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()
        self.ff.get("http://192.168.3.81/om/%E9%A6%96%E9%A1%B5.html")
        # self.ff.implicitly_wait(10) #设置网页打开超时时间
        self.ff.maximize_window()

    def tearDown(self):
        self.ff.close()

    def test_select_all(self):
        self.ff.find_element_by_id('u131').click()

        try:
            inputs=self.ff.find_element_by_id('userall').find_elements_by_tag_name('input')#.is_selected()
            for ipt in inputs:
                self.assertTrue(ipt.is_selected())
                #if not ipt.is_selected():
                #print 'tttttt'

        finally:
            pass

if __name__ == '__main__':
    unittest.main()