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

    def test_searchResultChart(self):
        '''
        按数量统计订单，查看结果分析图
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()
        self.driver.find_id('statistics_amount').click()
        text1=self.driver.find_element_by_class_name('order_title').text
        trs=self.driver.find_element_by_class_name('ui-jqgrid-sdiv').find_elements_by_tag_name('tr')
        tds=trs[len(trs)-1].find_elements_by_tag_name('td')
        success1=tds[1].text
        lose1=tds[2].text
        print success1,lose1

        self.driver.find_element_by_id('searchResultChart').click()
        self.driver.switch_to_alert()
        #显示结果分析图
        text2=self.driver.find_element_by_class_name('highcharts-title').text
        self.assertTrue(text1,text2)
        success2=self.driver.find_element_by_xpath('//*[@id="highcharts-0"]/svg/text[1]/tspan[1]').text
        lose2=self.driver.find_element_by_xpath('//*[@id="highcharts-0"]/svg/text[1]/tspan[2]').text
        print lose2,success2
        self.driver.find_element_by_link_text(u'关闭').click()
