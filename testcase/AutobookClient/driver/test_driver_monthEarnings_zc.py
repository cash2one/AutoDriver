# coding=utf-8
__author__ = 'gaoxu'

import datetime
from framework.core import idriver_android
import unittest
from framework.util import str


class TestCase(unittest.TestCase):
    #获取登录司机的工号
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    #返回首页
    def tearDown(self):
        self.driver.switch_to_home()

    #切换工作状态
    def test_my_info(self):
        self.driver.change_status(True)

        self.driver.find_id('rb_benifit').click()

        #点击收益
        current_activity = self.driver.current_activity
        #点击历史收益
        self.driver.find_id('about_function').click()
        self.driver.wait_switch(current_activity)
        current_activity = self.driver.current_activity
        self.driver.find_ids('rl')[0].click()
        self.driver.wait_switch(current_activity)
        orders=()
        ids=self.driver.find_ids('incomelist_in')

        for i in range(0,len(ids)):
            income=self.driver.find_ids('incomelist_in')[i].text[1:]
            order_income=str.to_long(income.split('.')[0]+income.split('.')[1])
            #获取屏幕上各记录的收益
            time=self.driver.find_ids('incomelist_time')[i].text
            order_time=str.to_datetime(time)
            #获取屏幕上各记录的时间
            order_order=self.driver.find_ids('incomelist_orderno')[i].text
            #获取屏幕上各记录的订单号
            orders+=((order_time,order_order,order_income),)
            #存入元组中
        month_orders=self.driver.sql('SELECT c.insert_time,a.order_no,(c.distance_charge-c.info_charge-c.insurance_charge) FROM t_order_info a, t_driver b,t_order_history c WHERE a.driver_id = b.id and a.id=c.order_info_id and b.no =%s ORDER BY a.create_time desc '% self.driver.no,0,1)
        #获取数据库中该司机的所有订单的收益情况
        print orders,month_orders



