# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import idriver
import datetime


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver.driver()
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_month_earning(self):
        self.driver.change_status(True)

        self.driver.find_element_by_id(self.driver.pkg + 'rb_benifit').click()
        self.driver.wait_find_id('he_td')
        sum_earning=self.driver.find_element_by_id(self.driver.pkg + 'he_sum').text

        current_activity = self.driver.current_activity
        self.driver.find_element_by_id(self.driver.pkg + 'about_function').click()
        self.driver.wait_switch(current_activity)
        earnings=0.00
        for i in range(0,3) :

            text_earning=self.driver.find_elements_by_id(self.driver.pkg + 'historyincome_income')[i].text
            earning=float(text_earning[1:])
            earnings+=earning
        self.assertTrue(unicode(earnings) in sum_earning)
