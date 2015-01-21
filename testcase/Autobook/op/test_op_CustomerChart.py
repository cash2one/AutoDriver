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

    def test_queryCustomer(self):
        '''
        点击新增走势图，查看图表内容
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()

        opts=self.driver.find_id('customerSource').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'平台注册':
                opt.click()
                self.assertTrue(opt.is_selected())

        self.driver.find_id('statistics').click()

        self.assertEqual(self.driver.title,u'客户统计列表')
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        startTime=trs[1].find_elements_by_tag_name('td')[0].text
        endTime=trs[len(trs)-1].find_elements_by_tag_name('td')[0].text
        self.driver.find_element_by_id('customerChart').click()
        text=self.driver.find_element_by_css_selector('#highcharts-0 > svg > text > tspan').text
        self.assertTrue(u'平台注册' in text)
        self.assertTrue(startTime in text)
        self.assertTrue(endTime[-3:] in text)

        self.driver.find_element_by_link_text(u'关闭').click()
        self.driver.find_element_by_id('back').click()
        self.assertEqual(self.driver.title,u'客户统计')
