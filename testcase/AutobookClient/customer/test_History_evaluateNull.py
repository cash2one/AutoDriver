# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'


import time
from drivers import *


class TestCase(unit.TestCase):
    '''
    历史订单的评价内容为空
    '''
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_Evaluate_History(self):
        '''
        评价内容为空
        :return:
        '''

        self.driver.wait_loading()
        #current_activity = self.driver.current_activity
        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()


        #点击历史订单
        personal_names = self.driver.find_ids('person_item')
        personal_names[1].click()
        self.driver.wait_loading()
         #判断是否有已完成订单
        try:
           list_text = self.driver.find_id('tv_notice').text
           if u'暂无已完成历史订单' in list_text :
               pass
        except:

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



    def test_Evaluate_null(self):
        '''
        不选择星星
        :return:
        '''
        self.driver.wait_loading()
        current_activity = self.driver.current_activity
        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()

        #点击历史订单
        personal_names = self.driver.find_ids('person_item')
        personal_names[1].click()
        self.driver.wait_loading()
         #判断是否有已完成订单
        try:
           list_text = self.driver.find_id('tv_notice').text
           if u'暂无已完成历史订单' in list_text :
               pass
        except:

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





