# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
import unittest
from framework.core import idriver_android
import datetime


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.driver()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_this_month_earning(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity
        self.driver.find_id('rb_benifit').click()

        he_td = self.driver.wait_find_id('he_td')
        td = he_td.text[1:]
        # 获取今日收益
        td_earning = filter(str.isdigit, str(td))
        # 去掉收益中的小数点
        cm = self.driver.find_id('he_cm').text[1:]
        #获取本月收益
        cm_earning = filter(str.isdigit, str(cm))

        today = datetime.date.today()
        #获取系统的日期
        this_month = filter(str.isdigit, str(today))[:-2]
        #获取的日期为2014-10-18的形式，去掉中间的符号,只获取到月

        amount = self.driver.sql(
            'select sum(amount) from t_statistics_driver_income where driver_no=' + self.driver.no + ' and s_month=' + this_month)
        #在数据库中查询昨日的收入

        info_charge = self.driver.sql(
            'select sum(info_charge) from t_statistics_driver_income where driver_no=' + self.driver.no + ' and s_month=' + this_month)
        #在数据库中查询昨日的服务费支出

        insurance_charge = self.driver.sql(
            'select sum(insurance_charge) from t_statistics_driver_income where driver_no=' + self.driver.no + ' and s_month=' + this_month)
        #在数据库中查询昨日的保险费支出
        earning1 = int(amount[0]) - int(info_charge[0]) - int(insurance_charge[0])
        #司机收入总和（数据库中只能查询到当前之前的数据）
        earning2 = int(cm_earning) - int(td_earning)
        print earning1, earning2
        self.assertTrue(earning1 == earning2)

