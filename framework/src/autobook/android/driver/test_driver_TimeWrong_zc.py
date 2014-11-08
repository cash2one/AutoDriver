# coding=utf-8
__author__ = 'zhangchun'

from framework.core import idriver
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver.driver()
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_TimeWrong(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity
        #获取待补订单列表中订单的信息
        self.driver.find_element_by_id(self.driver.pkg + 'iv_detail').click()
        self.driver.wait_switch(current_activity)

        self.driver.find_element_by_id(self.driver.pkg + 'ro_endtime').click()
        self.driver.switch_to_alert()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[1].click()
        self.driver.find_element_by_id(self.driver.pkg + 'btn_ok').click()
        self.driver.find_element_by_id(self.driver.pkg + 'confirm_repairorder').click()
        self.driver.switch_to_alert()

        txt=self.driver.find_element_by_id(self.driver.pkg + 'tv_msg').text
        self.assertTrue(u'结束时间不正确' in txt)