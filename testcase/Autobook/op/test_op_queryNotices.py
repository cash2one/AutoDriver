# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

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

    def test_queryNotice1(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()
        self.driver.find_id('noticeInfo').send_keys(u'通知')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        list_title=[]
        list_content=[]
        if len(trs)>1:
            for i in range(1,len(trs)-1):
                title=trs[i].find_elements_by_tag_name('td')[1].text
                content=trs[i].find_elements_by_tag_name('td')[2].text
                if u'通知'in title:
                    list_title.append(title)
                elif u'通知'in content:
                    list_content.append(content)
                time.sleep(3)
            self.assertTrue(len(list_title)>1 or len(list_content)>1)
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)
