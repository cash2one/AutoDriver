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
        startTime=self.driver.find_id('startTime_amount').text
        startTime1=filter(str.isdigit, str(startTime))
        endTime=self.driver.find_id('endTime_amount').text
        endTime1=filter(str.isdigit, str(endTime))
        print startTime1,endTime1
        self.driver.find_id('statistics_amount').click()
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        starttime=trs[1].find_elements_by_tag_name('td')[0].text
        print starttime
        startTime2=filter(str.isdigit, starttime)
        endtime=trs[len(trs)-1].find_elements_by_tag_name('td')[0].text
        endTime2=filter(str.isdigit, str(endtime))
        print startTime2,endTime2,endtime



