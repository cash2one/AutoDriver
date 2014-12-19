# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from framework.core import idriver_android
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_repair_order(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity
        #获取待补订单列表中订单的信息
        self.driver.find_id('iv_detail').click()
        self.driver.wait_switch(current_activity)

        self.driver.find_id('ro_endtime').click()
        self.driver.switch_to_alert()
        self.driver.find_tags('ImageButton')[6].click()
        self.driver.find_id('btn_ok').click()
        time.sleep(3)
        self.driver.find_id( 'ro_eaddr').send_keys('ggfdg')
        time.sleep(3)
        self.driver.find_id( 'confirm_repairorder').click()
        self.driver.switch_to_alert()

        txt=self.driver.find_id('tv_msg').text
        self.assertTrue(u'费用合计不能低于39元' in txt)

