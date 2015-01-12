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


    def test_querylog1(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()
        opts=self.driver.find_id('platformType').find_elements_by_tag_name('option')

        for opt in opts:
            if opt.get_attribute('text')==u'(运维)LXJ_OP_001':
                opt.click()
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件平台名称选择(运维)LXJ_OP_001
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[2].text
                self.assertEqual(text,u"(运维)LXJ_OP_001")
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)



    def test_querylog2(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()
        opts=self.driver.find_id('logType').find_elements_by_tag_name('option')

        for opt in opts:
            if opt.get_attribute('text')==u'用户日志':
                opt.click()
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件日志类型选择用户日志
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[3].text
                self.assertEqual(text,u"用户日志")
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)

    def test_querylog3(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()
        opts=self.driver.find_id('logLevel').find_elements_by_tag_name('option')

        for opt in opts:
            if opt.get_attribute('text')==u'信息':
                opt.click()
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件日志级别选择信息
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[4].text
                self.assertEqual(text,u"信息")
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_querylog4(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()

        self.driver.find_id('logInfo').send_keys(u'李嘉熙(zc01)')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件填写用户名称
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[5].text
                self.assertEqual(text,u"李嘉熙(zc01)")
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_querylog5(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()

        self.driver.find_id('logInfo').send_keys(u'192.168.3.81')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件填写用户IP
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[6].text
                self.assertEqual(text,u"192.168.3.81")
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_querylog6(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()

        self.driver.find_id('digest').send_keys(u'登录')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件填写用户名称
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[7].text
                self.assertEqual(text,u"登录")
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_querylog7(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()

        self.driver.find_id('content').send_keys(u'李嘉熙')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        #查询条件填写用户名称
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                text=trs[i].find_elements_by_tag_name('td')[7].text
                self.assertTrue(u'李嘉熙' in text)
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)