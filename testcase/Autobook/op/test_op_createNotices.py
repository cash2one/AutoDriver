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

    def test_addNotice(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()
        self.driver.find_id('create').click()
        self.driver.find_id('notice_title').send_keys(u'公告通知')
        self.driver.find_id('notice_content').send_keys(u'最近，凤凰台风来袭，注意关好窗户，防止衣服被刮走。')
        self.driver.find_id('allRole').click()
        self.driver.find_id('sure_btn').click()
        tds=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')
        title=tds[1].text
        content=tds[2].text
        self.assertEqual(u'公告通知',title)
        self.assertEqual(u'最近，凤凰台风来袭，注意关好窗户，防止衣服被刮走。',content)