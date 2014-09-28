__author__ = 'wangshanshan'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import atexit

class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff=webdriver.Firefox()
        self.url="http://112.124.117.108/tupu/table/"
        self.ff.maximize_window()
        time.sleep(1)
       # self.log_list=[]

    def tearDown(self):
        self.ff.quit()


    def test_list(self):
        self.ff.get(self.url)
        trs=self.ff.find_element_by_id('tableid').find_elements_by_tag_name('tr').find_elements_by_tag_name('td')
        for tr in trs:
            tds=tr.find_elements_by_tag_name('td')
            if tr.text=='hrrrrr':
                print tr.text

                print jsons['msg']['phone']










