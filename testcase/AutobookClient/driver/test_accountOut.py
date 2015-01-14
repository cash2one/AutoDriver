# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import datetime
from framework.core import testcase
from framework.util import strs
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_account(self):
        self.driver.change_status(True)
        current_activity = self.driver.current_activity
        self.driver.find_id('rb_benifit').click()
        self.driver.wait_find_id('he_td')
        self.driver.find_id('iv_right').click()
        #点击账户余额,进入收益tab页
        self.driver.wait_switch(current_activity)
        self.assertTrue('.AccountDetailsActivity',self.driver.current_activity)
        self.driver.find_id('ad_out').click()
        #进入支出页面

        ids=self.driver.find_ids("recharge_time")
        recharge_info1=()
        for i in range(0,len(ids)):
            time=self.driver.find_ids('recharge_time')[i].text
            recharge_time=strs.to_datetime(time)
            type=self.driver.find_ids('text')[i].text
            text_out=self.driver.find_ids('recharge_in')[i].text[1:]
            text_out1=text_out.split('.')[0]
            text_out2=text_out.split('.')[1]
            recharge_out=strs.to_long(text_out1+text_out2)
            recharge_info1+=((recharge_time,type,recharge_out,),)
        #获取一个屏幕的支出记录的信息（时间，类别，支出数目）

        print recharge_info1

        recharge_info2=self.driver.sql('SELECT a.insert_time,a.digest,order_out from t_driver_account_flow a,t_driver_account b where a.driver_account=b.id and b.driver_no='+self.driver.no,1,1)
        #获取数据库中该司机的全部支出记录
        print recharge_info2
        isExist = True
        for recharge in recharge_info1:
            if not recharge in recharge_info2:
               isExist = False
               break
        #系统中的支出记录信息应与数据库中的一致
        self.assertTrue(isExist,'false')
