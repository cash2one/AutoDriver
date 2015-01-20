# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_searchResultChart(self):
        '''
        按数量统计订单，查看结果分析图
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
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
        success2=self.driver.find_element_by_css_selector('#highcharts-0 > svg > text:nth-child(4) > tspan:nth-child(1)').text
        lose2=self.driver.find_element_by_css_selector('#highcharts-0 > svg > text:nth-child(4) > tspan:nth-child(2)').text

        self.assertTrue(success1 in success2)
        self.assertTrue(lose1 in lose2)
        self.driver.find_element_by_link_text(u'关闭').click()
        self.driver.find_element_by_link_text(u'返回').click()
        self.assertEqual(self.driver.title,u'订单统计')
