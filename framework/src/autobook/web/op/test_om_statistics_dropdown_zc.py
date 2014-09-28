__author__ = 'Administrator'
# coding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
#from util.fileUtil import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        #self.ff.implicitly_wait(10) #设置网页打开超时时间
        self.ff.implicitly_wait(10) #设置网页打开超时时间
        self.ff.maximize_window()
    def tearDown(self):
        self.ff.close()

    def test_1(self):
        self.ff.get("http://192.168.3.81/om/%E8%AE%A2%E5%8D%95%E7%BB%9F%E8%AE%A1.html") #测试网页地址
        self.ff.find_element_by_id('u66')#定位到下拉框
        time.sleep(5)
        self.ff.find_element_by_xpath("/html/body/div[1]/select[2]/option[2]").click()#选中下拉框选项
        time.sleep(5)#睡眠2S
        self.ff.find_element_by_id('u68').click()
        try:
            self.assertTrue('http://192.168.3.81/om/%E8%AE%A2%E5%8D%95%E7%BB%9F%E8%AE%A1_%E7%BB%93%E6%9E%9C.html' in self.ff.current_url)
            about_text=self.ff.find_element_by_id('u59_rtf').text
            self.assertTrue(u'统计查询' in about_text)
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'result'+os.sep+'geweg.png')
            pass

if __name__ =='__main__':
    unittest.main()
