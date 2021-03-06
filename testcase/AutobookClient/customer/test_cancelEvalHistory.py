# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()


    def test_cancel_EvalHistory(self):
        '''
        评价历史订单时，取消
        :return:
        '''
        current_activity = self.driver.current_activity
        self.driver.wait_loading()
        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()


        #点击历史订单
        personal_names = self.driver.find_ids('person_item')
        personal_names[1].click()
        self.driver.wait_loading()
        try :
           list_text = self.driver.find_id('tv_notice').text
           if u'暂无已取消历史订单' in list_text :
                pass
        except :

          order_Eval = self.driver.find_ids('order_Eval')[0].text
          print order_Eval

          #点击第2条评价
          self.driver.find_ids('order_finish_item')[0].click()
          self.driver.wait_loading()

          #选择星级            待完成
          self.driver.find_id('evaluate_ratingbar').click()
          self.driver.find_id('evaluate_content').send_keys('sbcde')
          self.driver.find_id('evaluate_submit').click()
          self.driver.switch_to_alert()
          tv_text = self.driver.find_id('tv_msg').text
          self.assertTrue(u'是否确认要提交' in tv_text,'msg')
          #点击取消
          self.driver.find_id('btn_cancel').click()















