# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import  idriver_android
import datetime


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.driver()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_my_yd(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity
        self.driver.find_element_by_id(self.driver.pkg + 'rb_benifit').click()
        self.driver.wait_find_id('he_td')
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        # 获取昨天的日期

        y = filter(str.isdigit, str(yesterday))
        #获取的日期为2014-10-18的形式，去掉中间的符号

        amount = self.driver.sql(
            'select sum(amount) from t_statistics_driver_income where driver_no=' + self.driver.no + ' and s_date=' + y)
        #在数据库中查询昨日的收入

        info_charge = self.driver.sql(
            'select sum(info_charge) from t_statistics_driver_income where driver_no=' + self.driver_no + ' and s_date=' + y)
        #在数据库中查询昨日的服务费支出

        insurance_charge = self.driver.sql(
            'select sum(insurance_charge) from t_statistics_driver_income where driver_no=' + self.driver.no + ' and s_date=' + y)
        #在数据库中查询昨日的保险费支出
        earning = int(amount[0]) - int(info_charge[0]) - int(insurance_charge[0])

        #收益=收入-服务费-保险费

        text_yd_earning = self.driver.find_element_by_id(self.driver.pkg + 'he_yd').text
        yd_earning = filter(str.isdigit, str(text_yd_earning[1:]))

        self.assertTrue(earning == int(yd_earning))







