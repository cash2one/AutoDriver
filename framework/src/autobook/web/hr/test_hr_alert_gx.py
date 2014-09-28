__author__ = 'gx'
# coding=utf-8
#hr_发布公告判断是否有弹出框测试

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from util.fileUtil import *
import os


class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()#打开火狐浏览器
        # self.ff.implicitly_wait(10) #设置网页打开超时时间

    #关闭
    def tearDown(self):
      self.ff.close()

    def test_test_popUpBox1(self):
      self.ff.get("http://192.168.3.81/hr/%E5%8F%B8%E6%9C%BA%E5%88%97%E8%A1%A8.html") #测试网页地址
          #浏览器最大化
      self.ff.maximize_window()
        #选择所有的input
      time.sleep(1)
      #点击按钮弹出对应框
      self.ff.find_element_by_id('u194_img').click()
      time.sleep(1)
      #判断是否有弹框
      try:
        alert = self.switch_to_alert()
        alert.accept()
      except:
        print 'no alert display '

