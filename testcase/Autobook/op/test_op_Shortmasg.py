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

    def test_Subplatform(self):
        '''

        可在其他选项中任意切换，该选项正常回显在文本框中
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        opts=self.driver.find_element_by_id('type').find_tags('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲

            if opt.get_attribute('text')==u'密码':
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')

    def test_Subplatformstate(self):
        '''

        可在其他选项中任意切换，该选项正常回显在文本框中
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        opts=self.driver.find_element_by_id('type').find_tags('option')
        self.assertTrue(opts[0].text==u'--短信类型--')
        tuple=(u'--短信类型--',u'验证码',u'密码')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')
            print(type)
            if not type in tuple:
                isExist = False
                break
        self.assertTrue(isExist,u'下拉框选项没有被选中')



    def test_Subplatformbox(self):
        '''
        可在其他选项中任意切换，该选项正常回显在文本框中
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        opts=self.driver.find_element_by_id('type').find_tags('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲

            if opt.get_attribute('text')==u'密码':
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')
            else:
                opt.get_attribute('text')==u'验证码'
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')


    def test_Subplatf(self):
        '''
        可在其他选项中任意切换，该选项正常回显在文本框中
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        opts=self.driver.find_element_by_id('state').find_tags('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲

            if opt.get_attribute('text')==u'--短信状态--':
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')

    def test_Subplatfstate(self):
        '''
        可在其他选项中任意切换，该选项正常回显在文本框中
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        opts=self.driver.find_element_by_id('state').find_tags('option')
        self.assertTrue(opts[0].text==u'--短信状态--')
        tuple=(u'--短信状态--',u'发送成功',u'发送失败')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')
            print(type)
            if not type in tuple:
                isExist = False
                break
        self.assertTrue(isExist,u'下拉框选项没有被选中')
