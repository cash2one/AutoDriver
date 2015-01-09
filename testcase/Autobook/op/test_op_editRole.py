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
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[1]/a').click()
        self.driver.find_id('editRole').click()
        #进入角色查看页面
        self.assertEqual(self.driver.title,u'编辑角色')
        self.driver.find_id('role_name').clear()
        self.driver.find_id('role_name').send_keys(u'客服管理员zw')
        self.driver.find_id('limits').click()
        self.driver.find_id('role_memo').clear()
        self.driver.find_id('role_memo').send_keys(u'此管理员拥有与之前相反的权限')
        self.driver.find_id('sure_edit_role_btn').click()
        text=self.driver.find_element_by_class_name('xubox_dialog').text
        print text
        self.assertTrue(u"编辑角色成功!"in text)
        self.driver.find_element_by_class_name('xubox_botton').click()

        # type=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text
        # name=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[2].text
        # memo=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[3].text
        # self.assertTrue(type==u'客服')
        # self.assertTrue(name==u'客服管理员zw')
        # self.assertTrue(memo==u'此管理员拥有与之前相反的权限')
