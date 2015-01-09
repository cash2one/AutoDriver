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

    def test_viewRole(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        type1=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text
        name1=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[2].text
        memo1=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[3].text
        self.driver.find_id('viewRole').click()
        #进入角色查看页面
        # name2=self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/input[2]').text
        # memo2=self.driver.find_id('role_memo').text
        # print name2,memo2
        # print memo1,name1
        # self.assertEqual(name1,name2)
        # self.assertEqual(memo1,memo2)
        self.assertEqual(self.driver.title,u'查看角色')
        self.driver.find_id('return_btn').click()
        self.assertEqual(self.driver.title,u'角色管理')
