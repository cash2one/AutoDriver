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
        self.ff= webdriver.Firefox()
        self.ff.get("http://192.168.3.81/om/%E8%B4%A6%E5%8F%B7%E7%AE%A1%E7%90%86_%E6%B7%BB%E5%8A%A0.html")
        # self.ff.implicitly_wait(10) #设置网页打开超时时间
        self.ff.maximize_window()

    def tearDown(self):
        self.ff.close()

    def initInputValue(self,ID,name,role,number,Email,comment):
        self.ff.find_element_by_id("u63").clear()
        self.ff.find_element_by_id("u63").send_keys(ID)

        self.ff.find_element_by_id("u69").clear()
        self.ff.find_element_by_id("u69").send_keys(name)
        time.sleep(1)
        self.ff.find_element_by_id("u63").find_element_by_xpath(role).click()
        time.sleep(1)

        self.ff.find_element_by_id('u79').clear()
        self.ff.find_element_by_id('u79').send_keys(number)

        self.ff.find_element_by_id('u81').clear()
        self.ff.find_element_by_id('u81').send_keys(Email)

        self.ff.find_element_by_id('u84').clear()
        self.ff.find_element_by_id('u84').send_keys(comment)

        self.ff.find_element_by_id('u67').click()

    def testID_1(self):
        self.initInputValue('','','/html/body/div[1]/select/option[1]','','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'必须填写用户ID'in text1)
        #finally:
            #pass

    def testID_2(self):
        self.initInputValue('12#3%','','/html/body/div[1]/select/option[1]','','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'用户ID格式有误'in text1)
        #finally:
            #pass

    def testname_1(self):
        self.initInputValue('admin','','/html/body/div[1]/select/option[1]','','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'必须填写用户姓名'in text1)
        #finally:
            #pass

    def testname_2(self):
        self.initInputValue('admin',u'管理员#%','/html/body/div[1]/select/option[1]','','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'用户姓名格式有误'in text1)
        #finally:
            #pass

    def testrole_1(self):
        self.initInputValue('admin',u'超级管理员','/html/body/div[1]/select/option[1]','','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'必须选择角色类别'in text1)
        #finally:
            #pass
    def testrole_2(self):
        self.initInputValue('admin',u'超级管理员','/html/body/div[1]/select/option[2]','','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'必须填写手机号码'in text1)
        #finally:
            #pass


        #finally:
            #pass

    def testnumber_2(self):
        self.initInputValue('admin',u'超级管理员','/html/body/div[1]/select/option[2]','139','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'手机号码格式有误'in text1)
        #finally:
            #pass

    def testnumber_3(self):
        self.initInputValue('admin',u'超级管理员','/html/body/div[1]/select/option[2]','13925561848444','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'手机号码格式有误'in text1)
        #finally:
            #pass

    def testnumber_1(self):
        self.initInputValue('admin',u'超级管理员','/html/body/div[1]/select/option[2]','13925561848','','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'必须填写Email'in text1)

    def testemail_1(self):
        self.initInputValue('admin',u'超级管理员','/html/body/div[1]/select/option[2]','13925561848','3121','')
        #try:
            #text1=self.ff.find_element_by_id('').text
            #self.assertTrue(u'Email格式有误'in text1)
        #finally:
            #pass

    def testemail_2(self):
        self.initInputValue('admin',u'超级管理员','/html/body/div[1]/select/option[2]','13925561848','3121@sina.cn','')
        try:
            self.assertTrue('http://192.168.3.81/om/%E8%B4%A6%E5%8F%B7%E7%AE%A1%E7%90%86.html'in self.ff.current_url)
            self.assertTrue('admin'in self.ff.find_element_by_id('u78_rtf').text)
            self.assertTrue(u'超级管理员'in self.ff.find_element_by_id('u80_rtf').text)
        finally:
            pass

if __name__ == '__main__':
    unittest.main()