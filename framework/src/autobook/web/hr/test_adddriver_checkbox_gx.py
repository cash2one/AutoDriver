__author__ = 'gaoxu'
# coding=utf-8
#hr_循环添加司机多选框测试lll

import time
import os
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from framework.core import device_bak


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    #关闭
    def tearDown(self):
        pass

    def test_checkbox1(self):
        device_bak.web().get("http://192.168.3.81/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html") #测试网页地址

        #选择所有的input
        opt= device_bak.web.find_elements_by_tag_name('input')
        for input in opt:
            #过滤出类型为checkbox的
            if input.get_attribute('type') == 'checkbox':
                #判断如果是checkbox类型的点击
                input.click()

       #self.ff.find_elements_by_css_selector('input[type=checkbox]')
        time.sleep(1)
    def test_checkbox2(self):
        device_bak.web.get("http://192.168.3.81/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html") #测试网页地址
          #浏览器最大化
        device_bak.web.maximize_window()
        #点击某一个
        device_bak.web.find_elements_by_css_selector('input[id=u86]').pop().click()


