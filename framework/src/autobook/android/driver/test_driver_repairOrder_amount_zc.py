# coding=utf-8
__author__ = 'zhangchun'

import time
from framework.core import idriver
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver.driver()
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_repair_order(self):
        self.driver.change_status(True)

        self.driver.find_element_by_id(self.driver.pkg + 'rb_benifit').click()
        self.driver.wait_find_id('he_td')
        he_td1=self.driver.find_element_by_id(self.driver.pkg + 'he_td').text[1:]
        #sum_td1=filter(str.isdigit,str(he_td1))
        #查看补单前的今日收益

        account_balance1=self.driver.find_element_by_id(self.driver.pkg + 'account_balance').text[1:]
        account1=account_balance1.split('(')[0]
        #查看补单前的账户余额

        self.driver.find_element_by_id(self.driver.pkg + 'rb_order').click()
        current_activity = self.driver.current_activity
        self.driver.find_element_by_id(self.driver.pkg + 'iv_detail').click()
        self.driver.wait_switch(current_activity)

        self.driver.find_element_by_id(self.driver.pkg + 'ro_endtime').click()
        self.driver.switch_to_alert()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[6].click()

        self.driver.find_element_by_id(self.driver.pkg + 'btn_ok').click()
        self.driver.find_element_by_id(self.driver.pkg + 'ro_eaddr').send_keys('ggfdg')
        self.driver.find_element_by_id(self.driver.pkg + 'ro_amount').send_keys('39')

        self.driver.find_element_by_id(self.driver.pkg + 'confirm_repairorder').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id(self.driver.pkg + 'btn_confirm').click()
        #补单成功

        self.driver.find_element_by_id(self.driver.pkg + 'rb_benifit').click()
        self.driver.wait_find_id('he_td')
        he_td2=self.driver.find_element_by_id(self.driver.pkg + 'he_td').text[1:]
        #查看补单后的今日收益
        account_balance2=self.driver.find_element_by_id(self.driver.pkg + 'account_balance').text[1:]
        account2=account_balance2.split('(')[0]
        #查看补单后的账户余额
        print he_td1,he_td2,account1,account2

        self.assertTrue(float(he_td2)-float(he_td1)==float(27.00))
        self.assertTrue(float(account1)-float(account2)==float(12.00))
