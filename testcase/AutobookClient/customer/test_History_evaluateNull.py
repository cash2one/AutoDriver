# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#历史订单的评价内容为空

import time
import unittest
from framework.core import idriver_android
from framework.util import str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()
    #评价内容为空
    def test_Evaluate_History(self):
        current_activity = self.driver.current_activity
        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()


        #点击历史订单
        personal_names = self.driver.find_ids('person_item')
        personal_names[1].click()
        self.driver.wait_loading()

        order_Eval = self.driver.find_ids('order_Eval')[1].text
        print order_Eval

        #点击第2条评价
        self.driver.find_ids('order_finish_item')[1].click()
        self.driver.wait_loading()

        #选择星级            待完成
        self.driver.find_id('evaluate_ratingbar').click()

        self.driver.find_id('evaluate_submit').click()

        self.driver.switch_to_alert()
        tv_text = self.driver.find_id('tv_msg').text
        self.assertTrue(u'是否确认要提交' in tv_text,'msg')
        self.driver.find_id('btn_ok').click()


    #不选择星星
    def test_Evaluate_null(self):
        current_activity = self.driver.current_activity
        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()


        #点击历史订单
        personal_names = self.driver.find_ids('person_item')
        personal_names[1].click()
        self.driver.wait_loading()

        order_Eval = self.driver.find_ids('order_Eval')[1].text
        print order_Eval

        #点击第2条评价
        self.driver.find_ids('order_finish_item')[1].click()
        self.driver.wait_loading()

        #选择星级            待完成
        #self.driver.find_id('evaluate_ratingbar').click()

        self.driver.find_id('evaluate_submit').click()

        self.driver.switch_to_alert()
        tv_text = self.driver.find_id('tv_msg').text
        self.assertTrue(u'亲,赏几颗星吧~' in tv_text,'msg')





