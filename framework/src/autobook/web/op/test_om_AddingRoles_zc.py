__author__ = 'zhangchun'
#coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
#from util.fileUtil import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.ff.implicitly_wait(10) #设置网页打开超时时间

        self.ff.maximize_window()

    def tearDown(self):
        self.ff.close()

    def test_1(self):
        self.ff.get("http://192.168.3.81/om/%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86_%E6%B7%BB%E5%8A%A0.html") #测试网页地址
        inputs = self.ff.find_elements_by_tag_name('input')#选择页面上所有的input，然后从中过滤出所有的checkbox并勾选之
        for input in inputs:
            if input.get_attribute('type') == 'checkbox':
                input.click()

                #checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
                #for checkbox in checkboxes:
                #checkbox.click()
        self.ff.find_elements_by_css_selector('input[type=checkbox]').pop().click()#取消选中最后一个复选框，即再次点击
        time.sleep(2)
    def test_2(self):
        self.ff.get("http://192.168.3.81/om/%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86_%E6%B7%BB%E5%8A%A0.html")
        self.ff.find_element_by_id("u112").click()
        time.sleep(2)
    def test_3(self):
        self.ff.get("http://192.168.3.81/om/%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86_%E6%B7%BB%E5%8A%A0.html")
        time.sleep(2)
        self.ff.find_element_by_id('u63').send_keys(u"财务人员")
        time.sleep(2)

        opts=self.ff.find_element_by_id('u68').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('value')==u'运维':
                opt.click()
                #break

        #dropdown.find_element_by_xpath("/html/body/div[1]/select/option[2]").click()
        time.sleep(4)
        self.ff.find_element_by_id("u112").click()
        time.sleep(2)
        self.ff.find_element_by_id('u69').send_keys(u'财务人员管理财务子平台')
        time.sleep(2)
        self .ff.find_element_by_id('u70').click()
        time.sleep(2)
        try:
            self.assertTrue('http://192.168.3.81/om/%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86.html' in self.ff.current_url)
            about_text=self.ff.find_element_by_id('u59_rtf').text
            self.assertTrue(u'角色管理' in about_text)
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'result'+os.sep+'geweg.png')
            pass

if __name__ =='__main__':
    unittest.main()

