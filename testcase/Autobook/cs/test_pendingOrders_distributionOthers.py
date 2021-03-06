# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    待处理订单页面：分配他人、取消
    '''
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_distributionOthers(self):
        '''
        #查询我的任务（订单来源默认）
        '''

        opts=self.driver.find_id('task').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'我的任务':
                opt.click()

        self.driver.find_id('query').click()
        time.sleep(2)

        self.driver.find_ajax_id('assign_other')
        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #取第一行第一列的订单号
        tds=trs[1].find_tags('td')
        order=tds[1].text
        print order
        #点击第一行的分配他人
        trs[1].find_id('assign_other').click()
        # self.driver.find_id('assign_other').click()
        text=self.driver.find_class('xubox_title').text
        print text
        self.assertTrue(u'分配他人' in text,'msg')
        #选择分配的人员
        opts1=self.driver.find_id('select_operator').find_tags('option')
        for opt1 in opts1:
            if opt1.get_attribute('text')==u'王晓晓':
                opt1.click()
        time.sleep(2)
        #点击分配按钮
        self.driver.find_id('assign_btn').click()
        time.sleep(2)
        text=self.driver.find_class('xubox_dialog').text
        print text
        self.assertTrue(u'分配成功！' in text,'msg')
        time.sleep(2)
        self.driver.find_link('确定').click()

        #查询被分配的订单
        self.driver.find_id('orderNo').send_keys(order)
        opts2=self.driver.find_id('task').find_tags('option')
        for opt in opts2:
            if opt.get_attribute('text')==u'全部任务':
                opt.click()

        self.driver.find_id('query').click()
        time.sleep(2)

        #在我的任务中找出第一行第一列的订单号和之前的比较
        trs1=self.driver.find_id('list').find_tags('tr')
        order2= trs1[1].find_tags('td')[1]
        name=trs1[1].find_tags('td')[9]

        if order2.get_attribute('title')==order and name.get_attribute('title')==u'王晓晓':
            pass
            print order2.get_attribute('title'), name.get_attribute('title')
        else:
            print '两个订单不相等'


    def test_distributionOthers_cancel(self):
        #查询我的任务（订单来源默认）
        opts=self.driver.find_id('task').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'我的任务':
                opt.click()

        self.driver.find_id('query').click()
        time.sleep(2)

        self.driver.find_ajax_id('assign_other')
        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #取第一行第一列的订单号
        tds=trs[1].find_tags('td')
        order=tds[1].text
        print order
        trs[1].find_id('assign_other').click()
        # self.driver.find_id('assign_other').click()
        text=self.driver.find_class('xubox_title').text
        print text
        self.assertTrue(u'分配他人' in text,'msg')
        time.sleep(2)
        self.driver.find_class('xubox_close').click()
        #在当前页面比较第一行第一列的订单是否相等
        trs1=self.driver.find_id('list').find_tags('tr')
        orders= trs1[1].find_tags('td')[1]
        if orders.get_attribute('title')==order:
            pass
            print orders.get_attribute('title')
        else:
            print '两个订单不相等'
