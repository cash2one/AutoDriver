__author__ = 'wangshanshan'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import atexit
from util.fileUtil import *
class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff=webdriver.Firefox()
        self.url="http://112.124.117.108/tupu/table/"
        self.ff.maximize_window()
        time.sleep(1)
       # self.log_list=[]

    def tearDown(self):
        self.ff.quit()

    def test_list1(self):
        self.ff.get(self.url)
        trs=self.ff.find_element_by_id('tableid').find_elements_by_tag_name('tr')

        # for tr in trs:
        #     tds=tr.find_elements_by_tag_name('td')
        #     for td in tds:
        #         print td.text

        for i in range(1,len(trs)):
            tds=trs[i].find_elements_by_tag_name('td')
            for j in range(0,len(tds)):
                if tds[j].text=='abc':
                    print tds[j].text



    def test_list2(self):
        self.ff.get(self.url)
        list=[]
        tds=self.ff.find_element_by_id('tableid').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')
        for td in tds:
            if td.text=='hr':
                list.append(td)
        try:

            self.assertTrue(len(list)>0)
        finally:
            pass