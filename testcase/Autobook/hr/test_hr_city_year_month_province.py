__author__ = 'lvfangying@pathbook.com.cn'
# coding=utf-8
#hr_循环验证用户名错误登录测试

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
# from util.fileUtil import *
import os


class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()#打开火狐浏览器
       #浏览器最大化
        self.ff.maximize_window()

    def testValue(self):
        #打开网址路径
        self.ff.get("http://192.168.3.31/hr/")
        time.sleep(3)
        #清除文本框中已有的数据
        self.ff.find_element_by_id('username').clear()
        #在文本框中输入值
        self.ff.find_element_by_id('username').send_keys("rs1202")

        self.ff.find_element_by_id('password').clear()
        #在文本框中输入值
        self.ff.find_element_by_id('password').send_keys("1138051554")
        time.sleep(5)

    def test_sex0(self):
        self.test_name0()
        # self.ff.find_element_by_id('bth_add').click()
        driverVo_sex=self.ff.find_element_by_id('driverVo_sex_tip').text
        self.assertTrue(u'请选择性别.'in driverVo_sex)
