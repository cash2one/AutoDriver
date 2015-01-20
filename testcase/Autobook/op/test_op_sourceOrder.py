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
        按来源统计订单，选择时间范围及订单结果
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        self.driver.find_id('li_source').click()
        opts=self.driver.find_id('orderResult').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'成功':
                opt.click()

        time.sleep(3)
        js = '$(\'input[id=startTime_source]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('startTime_source').clear()
        self.driver.find_id('startTime_source').send_keys('2015-01-02')

        js = '$(\'input[id=endTime_source]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('endTime_source').clear()
        self.driver.find_id('endTime_source').send_keys('2015-01-10')

        self.driver.find_id('statistics_source').click()
        self.assertEqual(self.driver.title,u'按来源统计')
        text=self.driver.find_element_by_css_selector('#highcharts-0 > svg > text.highcharts-title > tspan').text

        self.assertTrue(u'成功' in text)
        self.assertTrue(u'2015年01月02日' in text)
        self.driver.find_element_by_id('chart_back').click()
        self.assertEqual(self.driver.title,u'订单统计')


    def test_dateControl(self):
        '''
        结束时间小于开始时间，系统弹出提示框
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        self.driver.find_id('li_source').click()

        js = '$(\'input[id=startTime_source]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('startTime_source').clear()
        self.driver.find_id('startTime_source').send_keys('2015-01-02')

        js = '$(\'input[id=endTime_source]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_id('endTime_source').clear()
        self.driver.find_id('endTime_source').send_keys('2015-01-01')

        self.driver.find_id('statistics_source').click()
        text=self.driver.switch_to_alert().text
        self.assertEqual(text,u'开始日期不能大于截止日期，请重新选择日期！')
        self.driver.switch_to_alert().accept()