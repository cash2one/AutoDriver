# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    查询客户信息明细
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()
    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    def test_customerDetails(self):
        '''
        查看客户信息明细
        :return:
        '''
        self.driver.find_ajax_id('orderInfo_customer_name')

        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #点击第一行的客户信息
        trs[1].find_id('orderInfo_customer_name').click()
        time.sleep(2)
        self.driver.switch_to_alert()
        text=self.driver.find_class('xubox_title').text
        print text
        self.assertTrue(u'客户信息明细' in text,'客户信息明细不正确或不存在')

        # for tr in trs:
        #     tr.find_id('orderInfo_customer_name')

    def test_closeWindow(self):
        '''
        关闭客户信息明细窗口
        :return:
        '''
        self.driver.find_ajax_id('orderInfo_customer_name')

        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #点击第一行的客户信息
        trs[1].find_id('orderInfo_customer_name').click()
        #点击关闭按钮(关闭客户信息明细窗口)
        self.driver.find_link('关闭').click()
        time.sleep(2)
        isClose=True
        try:
            self.driver.find_id('xubox_main')
            isClose=False
        except self.driver.NoSuchElementException:
            isClose=True

        self.assertTrue(isClose,u'客户信息明细框没有被关闭')
        time.sleep(2)


