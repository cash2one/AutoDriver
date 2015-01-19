# coding=utf-8
__author__ = 'xhl'


import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from framework.core import testcase
import os
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()
    #查询分页
    def test_logall(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        ActionChains(self.driver).move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #点击末一页，是点击左后一夜的图标变灰
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
         #点击首页
        self.driver.find_element_by_id('first_pager').click()
        time.sleep(1)
        #点击下一页
        self.driver.find_element_by_id('next_pager').click()
        time.sleep(1)
        #点击上一页
        self.driver.find_element_by_id('prev_pager').click()
    #输入小数
    def test_logInput(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        ActionChains(self.driver).move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #跳转页数
        self.driver.find_element_by_class_name('ui-pg-input').send_keys("1" + Keys.RETURN)


    def test_Inputdecimal(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        ActionChains(self.driver).move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #跳转页数小数
        time.sleep(1)
        self.driver.find_element_by_class_name('ui-pg-input').send_keys("1.5" + Keys.RETURN)

    #输入非法字符
    def test_InputCharacters(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        ActionChains(self.driver).move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #跳转页数
        time.sleep(1)
        self.driver.find_element_by_class_name('ui-pg-input').send_keys("@@@" + Keys.RETURN)


    #输入超长字符
    def test_InputCharacter(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        ActionChains(self.driver).move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #跳转页数
        time.sleep(1)
        self.driver.find_element_by_class_name('ui-pg-input').send_keys("11111111111" + Keys.RETURN)
