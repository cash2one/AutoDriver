# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import unittest
from framework.core import idriver_android


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_sum_earning(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity
        self.driver.find_id('rb_benifit').click()

        self.driver.wait_find_id('he_td')
        td=self.driver.find_id('he_td').text[1:]
        #获取今日收益
        td_earning=filter(str.isdigit,str(td))
        #去掉收益中的小数点
        sd=self.driver.find_id('he_sum').text[1:]
        #获取累计收益
        sd_earning=filter(str.isdigit,str(sd))

        sum_amount=self.driver.sql('select sum(amount) from t_statistics_driver_income where driver_no=%s' % self.driver.no)
        #获取司机收入总和
        sum_info_charge=self.driver.sql('select sum(info_charge) from t_statistics_driver_income where driver_no=%s' % self.driver.no)
        #获取司机服务费总和
        sum_insurance_charge=self.driver.sql('select sum(insurance_charge) from t_statistics_driver_income where driver_no=%s' % self.driver.no)
        #获取司机保险费总和
        sum_earning=int(sum_amount[0])-int(sum_info_charge[0])-int(sum_insurance_charge[0])
        #司机收入总和（数据库中只能查询到当前之前的数据）
        earning=int(sd_earning)-int(td_earning)
        self.assertTrue(sum_earning==earning)
