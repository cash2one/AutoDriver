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

    def test_last_month_earning(self):
        idriver.changeWork(self.driver,True)

        current_activity = self.driver.current_activity
        self.driver.find_id('rb_benifit').click()
        self.driver.wait_find_id('he_td')
        td=self.driver.find_id('he_td').text[1:]
        #获取今日收益
        td_earning=filter(str.isdigit,str(td))
        #去掉收益中的小数点
        lm=self.driver.find_id('he_lm').text[1:]
        #获取上月收益
        lm_earning=filter(str.isdigit,str(lm))

        year=str(datetime.date.today().year)
        month=str(datetime.date.today().month)
        time=str(int(year+month)-1) #获取上个月的年月

        # time=datetime.date(datetime.date.today().year,datetime.date.month,1)-datetime.timedelta(1)
        # #获取本月第一天的前一天，在获取上个月的月份
        # last_month=filter(str.isdigit,str(time))[:-2]
        # #获取的日期为2014-10-18的形式，去掉中间的符号,只获取到月

        amount=self.driver.sql('select sum(amount) from t_statistics_driver_income where driver_no='+self.driver_no+' and s_month='+time)
        #在数据库中查询昨日的收入

        info_charge=self.driver.sql('select sum(info_charge) from t_statistics_driver_income where driver_no='+self.driver_no+' and s_month='+time)
        #在数据库中查询昨日的服务费支出

        insurance_charge=self.driver.sql('select sum(insurance_charge) from t_statistics_driver_income where driver_no='+self.driver_no+' and s_month='+time)
        #在数据库中查询昨日的保险费支出
        earning1=int(amount[0])-int(info_charge[0])-int(insurance_charge[0])
        #司机收入总和（数据库中只能查询到当前之前的数据）
        earning2=int(lm_earning)-int(td_earning)

        self.assertTrue(earning1==earning2)
        print earning1,earning2