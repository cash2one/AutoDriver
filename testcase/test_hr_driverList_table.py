__author__ = 'gx'
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        #self.ff.implicitly_wait(10) #设置网页打开超时时间
        self.verificationErrors=[]

    #关闭
    def tearDown(self):
        self.ff.close()
        self.assertTrue(len(self.verificationErrors)<=0)

    def test_driverList_table3(self):

       self.ff.get("http://112.124.117.108/")
       trs=self.ff.find_element_by_id('tableid').find_elements_by_tag_name('tr')

       for i in range(1,len(trs)):
           tds= trs[i].find_elements_by_tag_name('td')
           #self.assertTrue(tds[len(tds)-1].find_elements_by_link_text('del'))
           try:
               tds[len(tds)-1].find_element_by_link_text('del')
           except NoSuchElementException as e:
               self.verificationErrors.append(i)


