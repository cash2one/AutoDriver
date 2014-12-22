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
        time.sleep(1)
        self.ff.quit()


    def test_survey_pending(self):
        self.ff.get(self.url)
        self.ff.find_element_by_id('u72').click()
        try:
            self.assertTrue('http://192.168.3.81/cs/%E5%BE%85%E5%A4%84%E7%90%86%E8%AE%A2%E5%8D%95.html' in self.ff.current_url)
        finally:
            pass



    def test_survey_conduct(self):
        self.ff.get(self.url)
        self.ff.find_element_by_id('u74').click()
        try:
            self.assertTrue('http://192.168.3.81/cs/%E8%BF%9B%E8%A1%8C%E4%B8%AD%E8%AE%A2%E5%8D%95.html' in self.ff.current_url)
        finally:
            pass


    # def test_survey_archived(self):
    #     self.ff.get(self.url)
        # self.ff.find_element_by_id('u76').click()
        # try:
        #     self.assertTrue('http://192.168.3.81/cs/%E5%B7%B2%E5%BD%92%E6%A1%A3%E8%AE%A2%E5%8D%95.html' in self.ff.current_url)
        # finally:
        #     pass


    #def test_survey_suspension(self):
        #self.ff.get(self.url)
        #self.ff.find_element_by_id('u82').click()
        #try:
            #self.assertTrue('http://192.168.3.81/cs/%E5%B7%B2%E4%B8%AD%E6%AD%A2%E8%AE%A2%E5%8D%95.html' in self.ff.current_url)
        #finally:
            #pass


if __name__ =='__main__':
    unittest.main()