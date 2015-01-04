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


    def test_page_establish(self):
        self.ff.get(self.url)
        self.ff.find_element_by_id('u141').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.81/cs/%E5%88%9B%E5%BB%BA%E8%AE%A2%E5%8D%95_%E9%BB%98%E8%AE%A4%E9%A1%B5.html' in self.ff.current_url)
        finally:
            pass



    def test_page_pending(self):
        self.ff.get(self.url)
        self.ff.find_element_by_id('u142').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.40/cs/%E5%BE%85%E5%A4%84%E7%90%86%E8%AE%A2%E5%8D%95.html' in self.ff.current_url)
        finally:
            pass





if __name__ =='__main__':
    unittest.main()