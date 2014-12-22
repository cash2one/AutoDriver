__author__ = 'wangshanshan'
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
        # self.ff.implicitly_wait(10) #设置网页打开超时时间


    def tearDown(self):
        self.ff.close()

    def initInputValue(self,order_num,user_name,driver_name):
        self.ff.get("http://192.168.3.81/cs/%E5%BE%85%E5%A4%84%E7%90%86%E8%AE%A2%E5%8D%95.html")
        self.ff.maximize_window()
        time.sleep(1)
        self.ff.find_element_by_id('u141').send_keys(order_num)

        self.ff.find_element_by_id('u187').clear()
        self.ff.find_element_by_id('u187').send_keys(user_name)

        self.ff.find_element_by_id('u189').clear()
        self.ff.find_element_by_id('u189').send_keys(driver_name)
        opts=self.ff.find_element_by_id('u192').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('value')==u'平台下单':
                opt.click()
        self.ff.find_element_by_id('u142').click()

        
        try:
            self.assertTrue('http://192.168.3.81/cs/%E5%BE%85%E5%A4%84%E7%90%86%E8%AE%A2%E5%8D%95.html' in self.ff.current_url)
        finally:
            pass

    #def test_login_7(self):
        #self.initInputValue('gwegw','1323223','52323')

    def test_login_22(self):
        self.initInputValue('','','')



if __name__ == '__main__':
    unittest.main()