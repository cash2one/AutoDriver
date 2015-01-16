# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from framework.core import testcase
import datetime

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_datelist(self):
        '''
        选择开始时间及结束时间，提交后，列表中显示该时间范围内的订单记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        js = '$(\'input[id=startTime_amount]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime_amount').clear()
        time1='2015-01-06'
        self.driver.find_element_by_id('startTime_amount').send_keys(time1)
        #选择开始时间
        js = '$(\'input[id=endTime_amount]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime_amount').clear()
        time2='2015-01-15'
        self.driver.find_element_by_id('endTime_amount').send_keys(time2)
        self.driver.find_id('statistics_amount').click()
        #选择结束时间
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        start=trs[1].find_elements_by_tag_name('td')[0].text
        startTime=start[0:4]+'-'+start[5:7]+'-'+start[-3:-1]
        end=trs[len(trs)-1].find_elements_by_tag_name('td')[0].text
        endTime=end[0:4]+'-'+end[5:7]+'-'+end[-3:-1]
        self.assertEqual(time1,startTime)
        self.assertEqual(time2,endTime)
