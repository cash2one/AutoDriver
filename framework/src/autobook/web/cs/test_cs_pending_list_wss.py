__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import selenium.webdriver.support.ui as ui
from util.fileUtil import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.url='http://192.168.3.112/cs/%E5%BE%85%E5%A4%84%E7%90%86%E8%AE%A2%E5%8D%95.html'
        self.ff.maximize_window()
        time.sleep(2)

    def tearDown(self):
        self.ff.quit()

    def test_pending_list_customer(self):
        self.ff.get(self.url)
        self.ff.find_element_by_id('u86').click()

        time.sleep(1)


    # def test_pending_list_driver(self):
    #     self.ff.get(self.url)
        # self.ff.find_element_by_id('u88').click()



    # def test_pending_list_process(self):
    #     self.ff.get(self.url)
    #     self.ff.find_element_by_id('u99').click()
    #



    # def test_pending_list_communication(self):
    #     self.ff.get(self.url)
    #     time.sleep(20
        # self.ff.find_element_by_id('u193').click()



        try:
            alert = self.switch_to_alert()
            alert.accept()
        except:
            print 'no alerts display'



if __name__ =='__main__':
    unittest.main()