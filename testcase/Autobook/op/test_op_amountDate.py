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

    def test_orderSource(self):
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('dateType_amount').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'按天':
                opt.click()
        time.sleep(3)
        startTime=self.driver.find_id('startTime_amount')
        endTime=self.driver.find_id('endTime_amount')

        self.assertTrue(startTime.is_enabled()and endTime.is_enabled())

        for opt in opts:
            if opt.get_attribute('text')==u'按年':
                opt.click()
        time.sleep(3)
        startYear=self.driver.find_id('startYear')
        endYear=self.driver.find_id('endYear')

        self.assertTrue(startYear.is_enabled()and endYear.is_enabled())

        for opt in opts:
            if opt.get_attribute('text')==u'按月':
                opt.click()
        time.sleep(3)
        startMonth=self.driver.find_id('startMonth')
        endMonth=self.driver.find_id('endMonth')

        self.assertTrue(startMonth.is_enabled()and endMonth.is_enabled())



    def test_orderSource1(self):
        above=self.driver.find_element_by_link_text(u'日志查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        opts=self.driver.find_id('platformId').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'平台Id')
        tuple=(u'平台Id','APP_001','CS_001','CYL_OP_001','HEART_001','HR_001','HZL_HEART_001','HZL_HR_001','HZL_OP_001','IS_001','LCH_CS_001',
               'LXJ_CS_001','LXJ_HEART_001','LXJ_IS_001','LXJ_OP_001','NBY_APP_001','NBY_OP_001','OP_001','OP_002','STC_APP_001','STC_HEART_001',
               'STC_HR_001','STC_OP_001','ZCJ_CS_001','ZCJ_OP_001','ZMM_APP_001','ZMM_HEART_001','ZMM_HR_001','ZMM_OP_001')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break

        self.assertTrue(isExist,'false')
        #查看日志类型下拉框中的选项


