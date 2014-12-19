# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

from framework.core import idriver_android
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_TimeWrong(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity
        #获取待补订单列表中订单的信息
        self.driver.find_id('iv_detail').click()
        self.driver.wait_switch(current_activity)

        self.driver.find_id('ro_endtime').click()
        self.driver.switch_to_alert()
        self.driver.find_tags('ImageButton')[1].click()

        self.driver.find_id('btn_ok').click()
        self.driver.find_id('confirm_repairorder').click()
        self.driver.switch_to_alert()

        txt=self.driver.find_id('tv_msg').text
        self.assertTrue(u'结束时间不正确' in txt)