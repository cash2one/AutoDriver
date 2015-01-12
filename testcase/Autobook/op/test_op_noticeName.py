# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from framework.core import idriver_web
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_noticeName1(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()
        self.driver.find_element_by_id('create').click()
        self.driver.find_element_by_id('sure_btn').click()
        text1=self.driver.find_element_by_id('notice_title_tip').text
        text2=self.driver.find_element_by_id('notice_content_tip').text
        text3=self.driver.find_element_by_id('roleList_tip').text
        self.assertTrue(u'公告标题不能为空' in text1)
        self.assertTrue(u'公告内容不能为空' in text2)
        self.assertTrue(u'用户角色不能为空' in text3)

