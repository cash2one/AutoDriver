# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import device,idriver
import datetime


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        idriver.login_driver(self.driver)
        self.driver_no = idriver.get_driver_no()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_my_yd(self):
        idriver.changeWork(self.driver,True)

        current_activity = self.driver.current_activity()
        self.driver.find_id('rb_order').click()

        yesterday=datetime.date.today()-datetime.timedelta(days=1)
        #获取昨天的日期

        y=filter(str.isdigit,str(yesterday))
        #获取的日期为2014-10-18的形式，去掉中间的符号

        amount=self.driver.sql('select sum(amount) from t_statistics_driver_income where driver_no='+self.driver_no+' and s_date='+y)
        #在数据库中查询昨日的收入

        info_charge=self.driver.sql('select sum(info_charge) from t_statistics_driver_income where driver_no='+self.driver_no+' and s_date='+y)
        #在数据库中查询昨日的服务费支出

        insurance_charge=self.driver.sql('select sum(insurance_charge) from t_statistics_driver_income where driver_no='+self.driver_no+' and s_date='+y)
        #在数据库中查询昨日的保险费支出
        earning=int(amount[0])-int(info_charge[0])-int(insurance_charge[0])

        #收益=收入-服务费-保险费

        text_yd_earning=self.driver.find_id('he_yd').text
        yd_earning=filter(str.isdigit,str(text_yd_earning[1:]))

        self.assertTrue(earning==int(yd_earning))







