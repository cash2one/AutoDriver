# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    待处理订单页面：中止、取消中止
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_closeOrder(self):
        '''
        #中止订单
        :return:
        '''
        self.driver.find_ajax_id('closeOrder')
        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #取第一行第一列的订单号
        tds=trs[1].find_tags('td')
        order=tds[1].text
        print order
        #点击第一行的中止
        trs[1].find_id('closeOrder').click()
        self.driver.switch_to_alert()
        #比较弹出框信息内容是否正确
        text=self.driver.find_class('xubox_dialog').text
        print text
        self.assertTrue(u'确定中止该订单？' in text,'msg')
        #点击确定按钮
        self.driver.find_link('确定').click()
        time.sleep(3)


        #在当前页面比较第一行第一列的订单是否相等
        trs1=self.driver.find_id('list').find_tags('tr')
        orders= trs1[1].find_tags('td')[1]
        if orders.get_attribute('title')==order:
            pass
            print orders.get_attribute('title')
        else:
            print '两个订单不相等！！！'



    def test_cancel(self):
        '''
        #取消中止订单
        :return:
        '''
        self.driver.find_ajax_id('closeOrder')
        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #取第一行第一列的订单号
        tds=trs[1].find_tags('td')
        order=tds[1].text
        print order
        #点击第一行的中止
        trs[1].find_id('closeOrder').click()
        self.driver.switch_to_alert()
        #比较弹出框信息内容是否正确
        text=self.driver.find_class('xubox_dialog').text
        print text
        self.assertTrue(u'确定中止该订单？' in text,'msg')
        #点击确定按钮
        self.driver.find_link('取消').click()
        time.sleep(3)

        #在当前页面比较第一行第一列的订单是否相等
        trs1=self.driver.find_id('list').find_tags('tr')
        orders= trs1[1].find_tags('td')[1]
        if orders.get_attribute('title')==order:
            pass
            print orders.get_attribute('title')
        else:
            print '两个订单不相等'

