__author__ = 'gaoxu'
# coding=utf-8
#hr_添加司机出生年月测试
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
        #self.ff.implicitly_wait(10) #设置网页打开超时时间

    #关闭
    def tearDown(self):
        self.ff.close()
        #查看出生年月（年）下拉框选项
    def test_hr_selet1(self):
        #测试网页地址
        #self.ff.get("http://192.168.3.81/hr/")
        #self.ff.maximize_window()
        #self.ff.find_element_by_id('u6').click()#点击登录按钮
        self.ff.get("http://192.168.3.81/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html") #测试网页地址
        #睡眠3s
        time.sleep(1)
        #浏览器最大化
        self.ff.maximize_window()
         #睡眠3s
        time.sleep(1)
        #点击下拉框
        self.ff.find_element_by_id('u21').click()
         #睡眠5s


     #点击下拉框选中，显示在下拉框中
    def test_hr_selet2(self):
        self.ff.get("http://192.168.3.81/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html") #测试网页地址
        time.sleep(1)
        self.ff.maximize_window()
        opts=self.ff.find_element_by_id('u21').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts:
            if opt.get_attribute('value')=='1992':
                opt.click()

            #捕获异常
        try:
          self.assertTrue('http://192.168.3.81/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html' in self.ff.current_url)
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'result'+os.sep+'geweg.png')
            pass

           #查看出生年月（月）下拉框选项
    def test_hr_selet3(self):
        self.ff.get("http://192.168.3.81/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html") #测试网页地址
        #睡眠3s
        time.sleep(1)
        #浏览器最大化
        self.ff.maximize_window()
         #睡眠3s

        #点击下拉框
        self.ff.find_element_by_id('u22').click()
         #睡眠5s
        time.sleep(1)

     #点击下拉框选中，显示在下拉框中
    def test_hr_selet4(self):
        self.ff.get("http://192.168.3.81/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html") #测试网页地址
        time.sleep(1)
        self.ff.maximize_window()
        time.sleep(1)
        opts=self.ff.find_element_by_id('u22').find_elements_by_tag_name('option')

        for opt in opts:
            if opt.get_attribute('value')=='8':
                opt.click()

            #捕获异常
        try:
          self.assertTrue('http://192.168.3.81/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html' in self.ff.current_url)
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'result'+os.sep+'geweg.png')
            pass