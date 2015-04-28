# coding=utf-8
__author__ = 'xiaohengli@pathbook.com.cn'

import time
from drivers import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_sendfailed(self):
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        opts=self.driver.find_element_by_id('state').find_tags('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲
            if opt.get_attribute('text')==u'发送失败':
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')



    def test_sendSwitch(self):
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        opts=self.driver.find_element_by_id('state').find_tags('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲

            if opt.get_attribute('text')==u'发送失败':
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')
            else:
                opt.get_attribute('text')==u'发送成功'
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')

    def test_sendtest(self):
        '''
        输入内容正常显示在文本框中
        限制长度以内的字符正常显示，超出限制长度的部分系统限制输入
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        self.driver.find_element_by_id('smsHistoryInfo').send_keys(u'13636468711')
        text=self.driver.find_element_by_id('smsHistoryInfo').get_attribute('value')
        self.assertEqual(text,u'13636468711',u'找不到该号码')
        se=self.driver.find_element_by_id('smsHistoryInfo').text
        self.driver.find_element_by_id('smsHistoryInfo').send_keys(u'136364687111363646871113636468711136364687111363646871113636468711')
        time.sleep(3)
        text1=self.driver.find_element_by_id('smsHistoryInfo').get_attribute('value')
        self.assertEqual(text1,se,u'输入错误')


    def test_nullvalue(self):
        '''
        列表显示所有短信的监控记录
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        self.driver.find_element_by_id('query').click()