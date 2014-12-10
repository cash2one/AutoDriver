__author__ = 'gaoxu'
# coding=utf-8
#hr_循环添加司机姓名测试

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os


class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()#打开火狐浏览器
        # self.ff.implicitly_wait(10) #设置网页打开超时时间

    #关闭
    def tearDown(self):
        self.ff.close()

    #循环
    #self为关键字，user_name,user_pwd,login_button分别为三个参数
    def initInputValue(self,driver_name):
        #测试网页地址
        # self.ff.get("http://192.168.3.81/hr/")
        # self.ff.maximize_window()
        # self.ff.find_element_by_id('u6').click()
        #打开网址路径
        self.ff.get("http://192.168.3.31/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html")
        time.sleep(1)
        #浏览器最大化
        self.ff.maximize_window()
        #清除id为u11文本框中已有的数据
        self.ff.find_element_by_id('u11').clear()
        #在id为u11文本框中输入值
        self.ff.find_element_by_id('u11').send_keys(driver_name)
        time.sleep(1)
        self.ff.find_element_by_id('u60_img').click()
      #捕获异常
        try:
            self.assertTrue('http://192.168.3.31/hr/%E5%8F%B8%E6%9C%BA%E5%88%97%E8%A1%A8.html' in self.ff.current_url)
        finally:
             pass

    def InputValueerror(self,driver_name):
         #测试网页地址
        # self.ff.get("http://192.168.3.81/hr/")
        # self.ff.maximize_window()
        # self.ff.find_element_by_id('u6').click()
        #打开网址路径
        self.ff.get("http://192.168.3.31/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA.html")
        time.sleep(1)
        #浏览器最大化
        self.ff.maximize_window()
        #清除id为u4文本框中已有的数据
        self.ff.find_element_by_id('u11').clear()
        #在id为u11文本框中输入值
        self.ff.find_element_by_id('u11').send_keys(driver_name)
       # self.ff.find_element_by_id('u60_img').click()

        #捕获异常
        try:
            self.assertTrue('http://192.168.3.31/hr/%E6%B7%BB%E5%8A%A0%E5%8F%B8%E6%9C%BA' in self.ff.current_url)
        finally:
            pass

 #调用initInputValue，并输入正确的参数
    def test_driverName_1(self):
        self.initInputValue(u'张三')
     #调用initInputValue，并输入姓名不存在的参数
    def test_driverName_error2(self):
        self.InputValueerror('ghjrecf')
     #调用initInputValue，姓名为空，输入其他正确的参数
    def test_driverName_null3(self):
        self.InputValueerror('')
     #调用initInputValue，姓名超长，输入其他正确的参数
    def test_driverName_veryLong4(self):
        self.InputValueerror(u'张三张三张三张三张三张三张三张三')
     #调用initInputValue，姓名为数字，输入其他正确的参数
    def test_driverName_number5(self):
        self.InputValueerror('123123123')
       #调用initInputValue，姓名为特殊字符，输入其他正确的参数
    def test_driverName_specialCharacters6(self):
        self.InputValueerror('$#%&@*')

    #调用initInputValue，姓名前面加空格，输入其他正确的参数
    def test_driverName_frontBlankCharacter7(self):
        self.InputValueerror(u'  张三')

    #调用initInputValue，姓名中间加空格，输入其他正确的参数
    def test_driverName_middleBlankCharacter8(self):
        self.InputValueerror(u'张 三')

    #调用initInputValue，姓名后面加空格，输入其他正确的参数
    def test_driverName_rearBlankCharacter9(self):
        self.InputValueerror(u'张三  ')
