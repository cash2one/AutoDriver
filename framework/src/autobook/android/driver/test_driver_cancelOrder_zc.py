# coding=utf-8
__author__ = 'zhangchun'

import datetime
from framework.core import device,idriver
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        idriver.login_driver(self.driver)
        self.driver_no = idriver.get_driver_no()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_history_order(self):
        idriver.changeWork(self.driver,True)
        current_activity = self.driver.current_activity
        self.driver.find_id('iv_head').click()
        self.driver.wait_switch(current_activity)

        current_activity = self.driver.current_activity
        self.driver.find_element_by_name(u'历史订单').click()
        self.driver.wait_switch(current_activity)

        orders1_no=[]
        for i in range(0,5):
            text=self.driver.find_ids('order_number_text')[i].text
            order_no=text.split(':')[1].strip()
            orders1_no.append(order_no)

        orders2_no=self.driver.sql('SELECT a.order_no FROM t_order_info a, t_driver b WHERE a.driver_id = b.id and b.no =%s' % self.driver_no,1)

        print(type(orders1_no[1]))

        for j in range(0,len(orders1_no)-1):
            for i in range(0,len(orders2_no)-1):
                if orders1_no[j]!=orders2_no[i]:
                    i+=1
                    return i
                else:
                    j+=1
                    return j


