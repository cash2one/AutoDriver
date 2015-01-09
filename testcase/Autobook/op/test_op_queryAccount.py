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


    def test_stateQuery(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        opts=self.driver.find_id('state').find_elements_by_tag_name('option')

        for opt in opts:
            if opt.get_attribute('text')==u'禁用':
                opt.click()
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件状态选择禁用
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[4].text
                self.assertEqual(text,u"已禁用")
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)

    def test_nameQuery(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[2]/a').click()
        name='lishan'
        self.driver.find_id('operatorInfo').send_keys(name)

        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件填写登录名
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[1].text
                self.assertTrue(name in text)
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_realNameQuery(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[2]/a').click()
        realName=u'李三'
        self.driver.find_id('operatorInfo').send_keys(realName)

        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件填写登录名
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[2].text
                self.assertTrue(realName in text)
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_Query(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[2]/a').click()
        opts=self.driver.find_id('state').find_elements_by_tag_name('option')

        for opt in opts:
            if opt.get_attribute('text')==u'禁用':
                opt.click()
        name=u'zc'
        self.driver.find_id('operatorInfo').send_keys(name)

        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件状态为“禁用”，登录名为“zc”
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text1=trs[i].find_elements_by_tag_name('td')[1].text
                self.assertTrue(name in text1)
                text2=trs[i].find_elements_by_tag_name('td')[4].text
                self.assertTrue(u'已禁用' in text2)
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)