# coding=utf-8
__author__ = 'xiaohengli@pathbook.com.cn'

import time
from drivers import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_Subplatform(self):
        '''
       列表中显示所有符合查询条件的监控记录
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        self.driver.find_element_by_id('smsHistoryInfo').send_keys(u'13601677549')
        self.driver.find_element_by_id("query").click()
        trs=self.driver.find_element_by_id('list').find_tags('tr')
        print len(trs)
        #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in range(1,len(trs)):
                #找到td
                text=trs[i].find_tags('td')[1].text
                #判断是不是td里面的接口名称是不是driverService.dealOrder
                print text,i
                self.assertEqual(text,u"13601677549",u'没有这个用户')
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)