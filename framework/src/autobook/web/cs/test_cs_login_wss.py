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
        self.ff.maximize_window()
        time.sleep(1)
        # self.ff.implicitly_wait(10) #设置网页打开超时时间

    def tearDown(self):
        self.ff.close()

    def initInputValue(self,user_name,pwd,img_code):
        self.ff.get("http://192.168.3.81/cs/")

        self.ff.find_element_by_id('u4').clear()
        self.ff.find_element_by_id('u4').send_keys(user_name)

        self.ff.find_element_by_id('u5').clear()
        self.ff.find_element_by_id('u5').send_keys(pwd)

        self.ff.find_element_by_id('u10').clear()
        self.ff.find_element_by_id('u10').send_keys(img_code)

        self.ff.find_element_by_id('u6').click()

        try:
            self.assertTrue('http://192.168.3.81/cs/' in self.ff.current_url)
        finally:
            pass

    def test_login(self):
        self.initInputValue('wss111','123456','zfb3')

    #def test_login_user_empty(self):
        #self.initInputValue('','333','zfb3')

    def test_login_userpwd_empty(self):
        self.initInputValue('','','zfb3')

    #def  test_login_pwd_empty(self):
        #self.initInputValue('wss111','','zfb3')

    #def  test_login_code_empty(self):
        #self.initInputValue('wss111','123456','')

    #def  test_login_user_error(self):
        #self.initInputValue('wss222','123456','zfb3')

    #def  test_login_pwd_error(self):
        #self.initInputValue('wss111','123','zfb3')

    #def  test_login_code_error(self):
        #self.initInputValue('wss111','123456','1234')

    #def  test_login_user_special(self):
        #self.initInputValue(u'@#￥%…','123456','zfb3')

    #def  test_login_pwd_special(self):
        #self.initInputValue('wss111',u'@#$%','zfb3')

    #def  test_login_code_special(self):
        #self.initInputValue('wss111','123456',u'@#$%')

    #def  test_login_user_space(self):
        #self.initInputValue('wss  111','123456','zfb3')

    #def  test_login_pwd_space(self):
        #self.initInputValue('wss111','123  456','zfb3')

    #def  test_login_code_space(self):
        #self.initInputValue('wss111','123456','zf b 3')




if __name__ == '__main__':
    unittest.main()