__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
from util.fileUtil import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.url='http://192.168.3.81/cs/%E9%A6%96%E9%A1%B5_1.html'
        self.ff.maximize_window()
        time.sleep(1)

    def tearDown(self):
        self.ff.quit()


    def test_personal(self):
        self.ff.get(self.url)
        
        self.ff.find_element_by_id('u9').click()
        try:
            self.assertTrue('http://192.168.3.81/cs/%E4%B8%AA%E4%BA%BA%E8%AE%BE%E7%BD%AE_%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF.html' in self.ff.current_url)
        finally:
            pass


    def test_help(self):
        self.ff.get(self.url)

        self.ff.find_element_by_id('u5').click()
        try:
            self.assertTrue('http://192.168.3.81/cs/%E5%B8%AE%E5%8A%A9.html' in self.ff.current_url)
        finally:
            pass





if __name__ =='__main__':
    unittest.main()