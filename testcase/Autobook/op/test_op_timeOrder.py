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

    def test_sourceOrder(self):
        '''
        按时段统计订单，选择时间范围及订单来源及订单类型
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        self.driver.find_id('li_time').click()
        opts1=self.driver.find_id('orderSource_time').find_tags('option')
        for opt1 in opts1:
            if opt1.get_attribute('text')==u'客户下单':
                opt1.click()
                self.assertTrue(opt1.is_selected(),u'下拉框选项没有被选中')

        opts2=self.driver.find_id('orderType_time').find_tags('option')
        for opt2 in opts2:
            if opt2.get_attribute('text')==u'指定下单':
                opt2.click()
                self.assertTrue(opt2.is_selected(),u'下拉框选项没有被选中')

        js = '$(\'input[id=startTime_time]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('startTime_time').clear()
        self.driver.find_id('startTime_time').send_keys('2015-01-02')

        js = '$(\'input[id=endTime_time]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('endTime_time').clear()
        self.driver.find_id('endTime_time').send_keys('2015-01-11')

        self.driver.find_id('statistics_time').click()
        self.assertEqual(self.driver.title,u'订单统计列表')


        text=self.driver.find_element_by_css_selector('#highcharts-0 > svg > text.highcharts-title > tspan').text
        self.assertTrue(u'客户' in text)
        self.assertTrue(u'指定' in text)
        self.assertTrue(u'2015年01月02日' in text)

        self.driver.find_element_by_id('chart_back').click()
        self.assertEqual(self.driver.title,u'订单统计')



