# coding=utf-8
__author__ = 'zhangchun'

import time
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

    def test_repair_order(self):
        idriver.changeWork(self.driver,True)
        current_activity = self.driver.current_activity
        #获取待补订单列表中订单的信息
        self.driver.find_id('iv_detail').click()
        self.driver.wait_switch(current_activity)

        self.driver.find_id('ro_endtime').click()
        self.driver.switch_to_alert()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[6].click()

        self.driver.find_id('btn_ok').click()

        self.driver.find_id('confirm_repairorder').click()
        self.driver.switch_to_alert()

        txt=self.driver.find_id('tv_msg').text
        self.assertTrue(u'结束地点不能为空' in txt)
