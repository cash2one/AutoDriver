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


    def test_sameName(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('create').click()
        #进入角色添加页面
        self.driver.find_id('role_name').send_keys(u'财务超级管理8')
        self.driver.find_id('sure_create_role_btn').click()
        name=self.driver.switch_to_alert().text

        self.assertEqual(name,u'该用户已经存在!')
        self.driver.switch_to_alert().accept()