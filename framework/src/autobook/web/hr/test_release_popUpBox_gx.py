__author__ = 'gaoxu'
# coding=utf-8
#hr_循环发布公告弹出框测试

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

    #循环
    #self为关键字，idnumber
    def initInputValue(self,id_u4,id_u5):
        self.ff.get("http://192.168.3.81/hr/%E5%8F%B8%E6%9C%BA%E5%88%97%E8%A1%A8.html")
        #浏览器最大化
        self.ff.maximize_window()
        self.ff.find_element_by_id('u194_img').click()
        time.sleep(1)
        #打开网址路径
        self.ff.get("http://192.168.3.81/hr/%E5%8F%91%E5%B8%83%E5%85%AC%E5%91%8A.html")
        time.sleep(1)
        #浏览器最大化
        self.ff.maximize_window()
        #清除文本框中已有的数据
        self.ff.find_element_by_id('u4').clear()
        #在id为u80
        self.ff.find_element_by_id('u4').send_keys(id_u4)
        #time.sleep(1)
        self.ff.find_element_by_id('u5').clear()
        #在文本框中输入值
        self.ff.find_element_by_id('u5').send_keys(id_u5)
        #time.sleep(1)
        self.ff.find_element_by_id('u6_img').click()
        time.sleep(1)

     #捕获异常
        try:
            self.assertTrue('http://192.168.3.81/hr/%E5%8F%B8%E6%9C%BA%E5%88%97%E8%A1%A8.html' in self.ff.current_url)
        finally:
            pass


    def initInputValueerror(self,id_u4,id_u5):
        self.ff.get("http://192.168.3.81/hr/%E5%8F%B8%E6%9C%BA%E5%88%97%E8%A1%A8.html")
        #浏览器最大化
        self.ff.maximize_window()
        self.ff.find_element_by_id('u194_img').click()
        time.sleep(1)
        #打开网址路径
        self.ff.get("http://192.168.3.81/hr/%E5%8F%91%E5%B8%83%E5%85%AC%E5%91%8A.html")
        time.sleep(1)
        #浏览器最大化
        self.ff.maximize_window()
        self.ff.find_element_by_id('u4').clear()
        self.ff.find_element_by_id('u4').send_keys(id_u4)

        self.ff.find_element_by_id('u5').clear()
        self.ff.find_element_by_id('u5').send_keys(id_u5)
        time.sleep(1)  # 睡眠3S
        self.ff.find_element_by_id('u6_img').click()
         #捕获异常
        try:
            self.assertTrue('http://192.168.3.81/hr/%E5%8F%B8%E6%9C%BA%E5%88%97%E8%A1%A8.html' in self.ff.current_url)
        finally:
            pass


            #self为关键字，idnumber
    #调用initInputValue，并输入正确的参数
    def test_Announcement_correct(self):
     self.initInputValue(u'巴西足球赛',u'巴西1:7惨败德国，淘汰荷兰决战德国')

    def test_null_1(self):
        self.initInputValueerror('','')
    def test_null_2(self):
        self.initInputValueerror('rtrtn','')
    def test_null_3(self):
        self.initInputValueerror(u'类别类别类别类别类别类别','')
    def test_4(self):
        self.initInputValueerror(u' 类别',u' 规划和家人竟然有家人已经有软件可以人口')
    def test_5(self):
        self.initInputValueerror('',u' 飞刚好今天看图库竟然有家人已经')
    def test_6(self):
        self.initInputValueerror(u' 类 别',u' 一荣俱荣的法 规到好得很')
    def test_7(self):
        self.initInputValueerror(u' #@&%*&',u' 一荣俱荣的法 规到好得很')
    def test_7(self):
        self.initInputValueerror(u'类别',u' #@&%*1224&')
