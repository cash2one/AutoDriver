# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import datetime
from framework.core import idriver_android
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
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
        ids=self.driver.find_ids("recharge_time")
        recharge_info=()
        for i in range(0,len(ids)):
            time=self.driver.find_ids('recharge_time')[i].text
            text=self.driver.find_ids('text')[i].text
            recharge_in=self.driver.find_ids('recharge_in')[i].text
            recharge_info+=((time,text,recharge_in,),)
        print recharge_info
        str1=u'预付款充值'
        str1 =str1.decode(encoding='UTF-8', errors='strict')
        str2=u'入职付款'
        str2 =str2.decode(encoding='UTF-8', errors='strict')
        recharge_info1=self.driver.sql('SELECT a.insert_time,a.digest,a.pledge_in+a.prepay_in from t_driver_account_flow a,t_driver_account b where a.driver_account=b.id and b.driver_no='+self.driver.no+' and  (a.digest='+str1+' or a.digest='+str2+')',1,1)
        print recharge_info1



