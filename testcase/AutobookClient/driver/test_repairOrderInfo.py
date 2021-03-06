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

    def test_repair_Order(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity

        order_no =self.driver.find_ids('tv_order_id')[0].text

        order_time =self.driver.find_ids('tv_create_time')[0].text
        order_orgin =self.driver.find_ids('tv_start_address')[0].text
        txt_order=(order_no[4:],order_time,order_orgin[3:])
        #获取待补订单列表中订单的信息
        self.driver.find_id('iv_detail').click()
        self.driver.wait_switch(current_activity)

        ro_no=self.driver.find_id('ro_no').text
        ro_ctime=self.driver.find_id('ro_ctime').text
        ro_saddr=self.driver.find_id('ro_saddr').text
        txt_ro=(ro_no,ro_ctime,ro_saddr)
        #进入补单编辑页面，查看订单信息与列表中是否一致
        self.assertTrue(txt_ro==txt_order)
        self.assertTrue('.RepairOrderActivity',self.driver.current_activity)
