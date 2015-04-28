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

    def test_month_earning(self):
        self.driver.change_status(True)

        self.driver.find_id('rb_benifit').click()
        self.driver.wait_find_id('he_td')
        he_sum=self.driver.find_id('he_sum').text
        sum_earning=float(he_sum[1:])

        current_activity = self.driver.current_activity
        self.driver.find_id('about_function').click()
        self.driver.wait_switch(current_activity)
        months=self.driver.find_ids('rl')
        earnings=0.00
        for i in range(0,len(months)-1) :

            text_earning=self.driver.find_ids('historyincome_income')[i].text
            earning=float(text_earning[1:])
            earnings+=earning
        #计算各月份收益总和与累计收益是否相等
        self.assertTrue(earnings==sum_earning)

