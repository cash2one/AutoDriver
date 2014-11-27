# coding=utf-8
__author__ = 'gaoxu'

import datetime
from framework.core import idriver_android
import unittest
import time
from time import sleep


class TestCase(unittest.TestCase):
    #获取登录司机的工号
    def setUp(self):
        self.driver = idriver_android.driver()
        self.driver.login()

    #返回首页
    def tearDown(self):
        self.driver.switch_to_home()

    #切换工作状态
    def test_my_info(self):
        self.driver.change_status(True)
        #点击收益
        self.driver.find_id('rb_benifit').click()
        current_activity = self.driver.current_activity
        td=self.driver.find_id('he_td').text[1:]
        #获取今日收益
        td_earning=filter(str.isdigit,str(td))
        #去掉收益中的小数点
        self.driver.find_id('about_function').click()
        #点击历史收益
        self.driver.wait_switch(current_activity)


        tup_income=()
        income_id=self.driver.find_ids('historyincome_income')
        for i in range(0,len(income_id)):
            income_text=income_id[i].text
            income=filter(str.isdigit, str(income_text[1:]))
            if income==str("000"):
                tup_income+=('0',)
            else:
                tup_income+=(income,)

        print tup_income,str("000")

        tup_month=()
        month_id=self.driver.find_ids('historyincome_time')
        for i in range(0,len(month_id)):
            month_text=month_id[i].text
            month=month_text[0:4]+month_text[-3:-1]
            tup_month+=(month,)
        print tup_month

        tup_earning=()
        e=self.driver.sql('SELECT sum(amount-info_charge-insurance_charge) from t_statistics_driver_income where driver_no='+self.driver.no+' and s_month='+tup_month[0])
        this_mouth_Earning=int(e[0]+int(td_earning))
        tup_earning+=(str(this_mouth_Earning),)
        for i in range(1,len(month_id)):
            earning=self.driver.sql('SELECT sum(amount-info_charge-insurance_charge) from t_statistics_driver_income where driver_no='+self.driver.no+' and s_month='+tup_month[i])

            tup_earning+=(str(earning[0]),)
        print tup_earning,this_mouth_Earning
        self.assertTrue(tup_earning==tup_income)