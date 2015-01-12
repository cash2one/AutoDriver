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


    def test_createAccount(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        n='lishan2'
        r=u'李三2'
        self.driver.find_id('operator_name').send_keys(n)
        self.driver.find_id('operator_realName').send_keys(r)
        ipts=self.driver.find_id('pf2_roles').find_elements_by_tag_name('input')
        for ipt in ipts:
            if ipt.get_attribute('title')==u'客服经理':
                ipt.click()
                self.assertTrue(ipt.is_displayed)
        self.driver.find_id('operator_mobile').send_keys(u'18155364561')
        self.driver.find_id('operator_email').send_keys(u'18155@qq.com')

        self.driver.find_id('sure_create_account_btn').click()
        self.driver.switch_to_alert()
        text=self.driver.find_element_by_class_name('xubox_dialog').text
        self.assertTrue(u'创建账号成功'in text)
        self.driver.find_element_by_link_text(u'确定').click()

        name=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text
        realName=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[2].text
        role=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[3].text
        self.assertTrue(n in name)
        self.assertTrue(r in realName)
        self.assertTrue(u'客服经理'in role)