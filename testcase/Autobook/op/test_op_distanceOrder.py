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
        按里程统计订单，选择时间范围及订单来源及订单类型
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        self.driver.find_id('li_dis').click()
        opts1=self.driver.find_id('orderSource_dis').find_tags('option')
        for opt1 in opts1:
            if opt1.get_attribute('text')==u'客户下单':
                opt1.click()
                self.assertTrue(opt1.is_selected())

        opts2=self.driver.find_id('orderType_dis').find_tags('option')
        for opt2 in opts2:
            if opt2.get_attribute('text')==u'指定下单':
                opt2.click()
                self.assertTrue(opt2.is_selected())

        js = '$(\'input[id=startTime_dis]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('startTime_dis').clear()
        self.driver.find_id('startTime_dis').send_keys('2015-01-02')

        js = '$(\'input[id=endTime_dis]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('endTime_dis').clear()
        self.driver.find_id('endTime_dis').send_keys('2015-01-15')

        self.driver.find_id('statistics_dis').click()

        self.assertEqual(self.driver.title,u'按里程数统计')
        text=self.driver.find_element_by_css_selector('#highcharts-0 > svg > text.highcharts-title > tspan').text

        self.assertTrue(u'客户' in text)
        self.assertTrue(u'指定' in text)
        self.assertTrue(u'2015年01月02日' in text)
        self.driver.find_element_by_id('chart_back').click()
        self.assertEqual(self.driver.title,u'订单统计')


    def test_dateControl(self):
        '''
        结束时间小于开始时间，系统弹出提示框'开始日期不能大于截止日期，请重新选择日期！'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        self.driver.find_id('li_dis').click()

        js = '$(\'input[id=startTime_dis]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('startTime_dis').clear()
        self.driver.find_id('startTime_dis').send_keys('2015-01-02')

        js = '$(\'input[id=endTime_dis]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('endTime_dis').clear()
        self.driver.find_id('endTime_dis').send_keys('2015-01-01')

        self.driver.find_id('statistics_dis').click()
        text=self.driver.switch_to_alert().text
        self.assertEqual(text,u'开始日期不能大于截止日期，请重新选择日期！')
        self.driver.switch_to_alert().accept()