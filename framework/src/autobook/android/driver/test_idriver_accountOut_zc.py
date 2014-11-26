# coding=utf-8
__author__ = 'zhangchun'

import datetime
from framework.core import idriver_android
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.driver()
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

        ids=self.driver.find_ids("recharge_time")
        recharge_info1=()
        for i in range(0,len(ids)):
            time=self.driver.find_ids('recharge_time')[i].text
            text=self.driver.find_ids('text')[i].text
            recharge_in=self.driver.find_ids('recharge_in')[i].text
            recharge_info1+=((time,text,recharge_in,),)
            print time[0]. timetuple ()
        print recharge_info1

        #
        # recharge_info2=self.driver.sql('SELECT a.insert_time,a.digest,order_out from t_driver_account_flow a,t_driver_account b where a.driver_account=b.id and b.driver_no='+self.driver.no,'fa',1)
        #
        # isExist = True
        # for recharge in recharge_info1:
        #     if not recharge in recharge_info2:
        #         isExist = False
        #         break
        # print recharge_info1
        # print recharge_info2
        #self.assertTrue(isExist,'false')
