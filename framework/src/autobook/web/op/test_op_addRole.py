__author__ = 'zhangchun@pathbook.com.cn'
# coding=utf-8
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


    def test_role_name(self):

        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[1]/a').click()
        self.driver.find_id('create').click()
        #进入角色添加页面
        self.assertEqual(self.driver.title,u'添加角色')
        self.driver.find_id('sure_create_role_btn').click()
        text=self.driver.find_id('role_name_tip').text
        print text
        self.assertEqual(text,u'角色名称不能为空.')

    def test_add_success(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[1]/a').click()
        self.driver.find_id('create').click()
        #进入角色添加页面
        self.driver.find_id('role_name').send_keys(u'财务超级管理9')
        self.driver.find_id('sure_create_role_btn').click()
        self.driver.switch_to_alert()

        time.sleep(2)
        text=self.driver.find_element_by_class_name('xubox_main').text
        self.assertTrue(u"添加角色成功" in text)
        self.driver.find_element_by_xpath(u'/html/body/div[5]/div[1]/span[2]/a').click()
        self.driver.wait_find_id('')
        name=self.driver.find_id('list').find_elements_by_class_name('tr')[1].find_elements_by_class_name('td')[2].text
        self.assertTrue(name==u'财务超级管理9')





