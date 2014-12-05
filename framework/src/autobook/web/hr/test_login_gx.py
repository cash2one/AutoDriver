__author__ = 'gaoxu'
# coding=utf-8
#hr_循环验证用户名错误登录测试

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
# from util.fileUtil import *
from framework.core import idriver_web
import os


class TestCase(unittest.TestCase):
    def setUp(self):
        # self.ff = webdriver.Firefox()#打开火狐浏览器
        # self.ff.implicitly_wait(10) #设置网页打开超时时间
        self.driver = idriver_web.firefox(__file__)

    #关闭
    def tearDown(self):
        self.driver.close()

       #循环
    #self为关键字，user_name,user_pwd,login_button分别为三个参数
    def initInputValue(self,user_name,user_pwd,user_captcha):
        #打开网址路径
        self.driver.get("http://192.168.3.31/hr/")
        time.sleep(1)
        #浏览器最大化
        self.driver.maximize_window()
        #清除id为u4文本框中已有的数据
        time.sleep(1)
        #清除id为u4文本框中已有的数据
        self.driver.find_element_by_id('username').clear()
        #在id为u4文本框中输入值
        self.driver.find_element_by_id('username').send_keys(user_name)
        #清除id为u5文本框中已有的数据
        self.driver.find_element_by_id('password').clear()
        #time.sleep(3)
        #self.ff.execute_script(u"alert('用户名输入有误！')")
       # time.sleep(3)
        #在id为u5文本框中输入值
        self.driver.find_element_by_id('password').send_keys(user_pwd)
        #清除id为u10文本框中已有的数据
        self.driver.find_element_by_id('captcha').clear()
        #在id为u10文本框中输入值
        self.driver.find_element_by_id('captcha').send_keys(user_captcha)
        #睡眠3S
        time.sleep(1)
        #点击id为u6的按钮
        self.driver.find_element_by_id('login').click()
         #捕获异常
        try:
            self.assertTrue('http://192.168.3.31/hr/hr/driver/addDriver.html' in self.driver.current_url)
        finally:
            pass



    #循环
    #self为关键字，user_name,user_pwd,login_button分别为三个参数
    def initInputValueerror(self,user_name):
        #打开网址路径
        self.driver.get("http://192.168.3.31/hr/")
        time.sleep(1)
        #浏览器最大化
        self.driver.maximize_window()
        #清除id为u4文本框中已有的数据
        time.sleep(1)
        #清除id为u4文本框中已有的数据
        self.driver.find_element_by_id('username').clear()
        #在id为u4文本框中输入值
        self.driver.find_element_by_id('username').send_keys(user_name)
        #清除id为u5文本框中已有的数据
        self.driver.find_element_by_id('password').clear()
        #点击id为u6的按钮
        #self.ff.find_element_by_id('u6').click()
        try:
            self.assertTrue('http://192.168.3.31/hr' in self.driver.current_url)
        finally:
            pass

    #调用initInputValue，并输入正确的参数
    def test_correct_value(self):
        self.initInputValue('abc','123456','zfb3')
     #调用initInputValue，并输入用户名不存在的参数
    def test_userName_noTexist1(self):
        self.initInputValueerror('ghjrecf')
     #调用initInputValue，用户名为空，输入其他正确的参数
    def test_userName_null2(self):
        self.initInputValueerror('')
      #  self.error(u'用户名不能为空！')
     #调用initInputValue，用户名超长，输入其他正确的参数
    def test_userName_veryLong3(self):
        self.initInputValueerror('aaaaaaaaaaaaaaaaaaaaaaaaaaa')

     #调用initInputValue，用户名为数字，输入其他正确的参数
    def test_userName_number4(self):
        self.initInputValueerror('123123123')
       #调用initInputValue，用户名为特殊字符，输入其他正确的参数
    def test_userName_specialCharacters5(self):
        self.initInputValueerror('$#%&@*')

    #调用initInputValue，用户名前面加空格，输入其他正确的参数
    def test_userName_frontBlankCharacter6(self):
        self.initInputValueerror('  aaa')

    #调用initInputValue，用户名中间加空格，输入其他正确的参数
    def test_userName_middleBlankCharacter7(self):
        self.initInputValueerror('a aa')

    #调用initInputValue，用户名后面加空格，输入其他正确的参数
    def test_userName_rearBlankCharacter8(self):
        self.initInputValueerror('aaa ')
