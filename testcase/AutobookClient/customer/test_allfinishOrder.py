# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'


import time
import unittest
from framework.core import testcase

class TestCase(unittest.TestCase):
    '''
    查询第一屏已完成的历史订单并判断在数据库中
    '''
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_allfinishOrder(self):
        # activity = self.driver.current_activity
        # layout_ids = self.driver.layout[activity]
        #点击用户中心图标，进入用户中心列表
        # self.driver.find_id(layout_ids['btn_personal_center']).click()
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()
        #点击历史订单
        self.driver.find_ids('person_item')[1].click()
        self.driver.wait_loading()

        #判断是否有已完成订单
        try:
           list_text = self.driver.find_id('tv_notice').text
           if u'暂无已完成历史订单' in list_text :
               pass
        except:
            #获取所有已完成订单列表的订单号
            orders_no=()
            order = self.driver.find_ids('order_no')
            for i in range(0,len(order)-1):
                order_Nos=self.driver.find_ids('order_no')[i].text
                orders_no+=((order_Nos,),)
                print orders_no

                #从数据库中获取所有订单号
                sql_order=self.driver.sql('SELECT order_no FROM t_order_info where customer_id=34' ,0,1)
                print sql_order

                #判断若有一个订单不在数据库中跳出
                isExist = True
                for no in orders_no:
                   if no not in sql_order:
                    isExist = False
                    break
                self.assertTrue(isExist,'false')


