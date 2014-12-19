# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#用户登录，历史订单已取消订单为空（暂无已取消历史订单）

import time

import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()


    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_cancelOrdernull(self):
        self.driver.find_id('btn_personal_center').click()
        #点击历史订单
        self.driver.find_ids('person_item')[1].click()
        #点击已取消按钮
        self.driver.find_id('iscancle').click()
        #对比
        text=self.driver.find_id('tv_notice').text
        print text
        self.assertTrue(u'暂无已取消历史订单' in text ,'msg')