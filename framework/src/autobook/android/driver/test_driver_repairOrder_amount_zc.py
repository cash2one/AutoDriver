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

        self.driver.find_id('rb_benifit').click()
        self.driver.wait_find_id('he_td')
        he_td1=self.driver.find_id('he_td').text[1:]
        #sum_td1=filter(str.isdigit,str(he_td1))
        #查看补单前的今日收益

        account_balance1=self.driver.find_id('account_balance').text[1:]
        account1=account_balance1.split('(')[0]
        #查看补单前的账户余额

        self.driver.find_id('rb_order').click()
        current_activity = self.driver.current_activity
        self.driver.find_id('iv_detail').click()
        self.driver.wait_switch(current_activity)

        self.driver.find_id('ro_endtime').click()
        self.driver.switch_to_alert()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[6].click()

        self.driver.find_id('btn_ok').click()
        self.driver.find_id('ro_eaddr').send_keys('ggfdg')
        self.driver.find_id('ro_amount').send_keys('39')

        self.driver.find_id('confirm_repairorder').click()
        self.driver.switch_to_alert()
        self.driver.find_id('btn_confirm').click()
        #补单成功

        self.driver.find_id('rb_benifit').click()
        self.driver.wait_find_id('he_td')
        he_td2=self.driver.find_id('he_td').text[1:]
        #查看补单后的今日收益
        account_balance2=self.driver.find_id('account_balance').text[1:]
        account2=account_balance2.split('(')[0]
        #查看补单后的账户余额
        print he_td1,he_td2,account1,account2

        self.assertTrue(float(he_td2)-float(he_td1)==float(27.00))
        self.assertTrue(float(account1)-float(account2)==float(12.00))
