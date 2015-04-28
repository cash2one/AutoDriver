# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_status_suspension(self):
        '''
        查询条件选择状态为：中止
        :return:
        '''
        time.sleep(1)
        self.driver.find_ajax_id('main_menu')
        # self.driver.find_id('main_menu').click()
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('历史订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/listOrderHistory.html' in self.driver.current_url,u'不是历史订单页面')
        finally:
            pass
        opts=self.driver.find_id('orderState').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'中止':
                opt.click()
        self.driver.find_id('query').click()
        time.sleep(1)
        trs=self.driver.find_id('list').find_tags('tr')
        #取第一行第3列的订单号
        for i in range(1,len(trs)-1):
            tds=trs[i].find_tags('td')[8]
            print tds.text
        self.assertEqual(u'中止',tds.text,u'查询结果中有不是中止的订单')


    def test_status_file(self):
        '''
        查询条件选择状态为：归档
        :return:
        '''
        time.sleep(1)
        self.driver.find_ajax_id('main_menu')
        # self.driver.find_id('main_menu').click()
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('历史订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/listOrderHistory.html' in self.driver.current_url,u'不是历史订单页面')
        finally:
            pass
        opts=self.driver.find_id('orderState').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'归档':
                opt.click()
        self.driver.find_id('query').click()
        time.sleep(1)
        trs=self.driver.find_id('list').find_tags('tr')
        #取第一行第3列的订单号
        for i in range(1,len(trs)-1):
            tds=trs[i].find_tags('td')[8]
            print tds.text
        self.assertEqual(u'归档',tds.text,u'查询结果中有不是归档的订单')
