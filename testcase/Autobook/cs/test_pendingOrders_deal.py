# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    待处理订单页面：我要处理（确定）、取消
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #我要处理该订单
    def test_deal(self):
        self.driver.find_ajax_id('deal')

        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #取第一行第一列的订单号
        tds=trs[1].find_tags('td')
        order=tds[1].text
        print order
        #点击第一行的我要处理
        trs[1].find_id('deal').click()
        #比较弹出框信息内容是否正确
        text=self.driver.find_class('xubox_dialog').text
        print text
        self.assertTrue(u'确定处理该订单？' in text,'msg')

        self.driver.find_link('确定').click()
        time.sleep(2)

        #查询我的任务
        opts=self.driver.find_id('task').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'我的任务':
                opt.click()
        self.driver.find_id('query').click()
        time.sleep(3)

        #在我的任务中找出第一行第一列的订单号和之前的比较
        trs1=self.driver.find_id('list').find_tags('tr')
        orders= trs1[1].find_tags('td')[1]
        print orders
        if orders.get_attribute('title')==order:
            pass
            print orders.get_attribute('title')
        else:
            print '两个订单不相等'

        # #判断若有一个订单不在数据库中跳出
        #     isExist = True
        #     for no in order:
        #         if no not in orders:
        #          isExist = False
        #          break
        #     self.assertTrue(isExist,'false')

    #
    def test_cancel(self):
        self.driver.find_ajax_id('deal')

        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #取第一行第一列的订单号
        tds=trs[1].find_tags('td')
        order=tds[1].text
        print order
        #点击第一行的我要处理
        trs[1].find_id('deal').click()
        self.driver.switch_to_alert()
        self.driver.find_link('取消').click()
        time.sleep(2)

        #找出第一行第一列的订单号和之前的比较
        table1=self.driver.find_id('list')
        trs1=table1.find_tags('tr')
         #在订单列查找我要处理的订单号
        # for i in range(1,len(trs1)-1):
        orders= trs1[1].find_tags('td')[1]
        if orders.get_attribute('title')==order:
            pass
            print orders.get_attribute('title')
        else:
            print '两个订单不相等'





