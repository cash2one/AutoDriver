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

    def test_selectAllLimit(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('create').click()
        #进入角色添加页面
        self.driver.find_id('allLimit').click()
        #点击全选复选框，权限选项全部被选中
        try:
            inputs=self.driver.find_id('limitsList').find_elements_by_tag_name('input')
            for ipt in inputs:
                self.assertTrue(ipt.is_selected())
        finally:
            pass


        self.driver.find_id('reverseCheck').click()
        #点击反选复选框，权限选项全部被取消选中
        try:
            inputs=self.driver.find_id('limitsList').find_elements_by_tag_name('input')
            for ipt in inputs:
                self.assertFalse(ipt.is_selected())
        finally:
            pass