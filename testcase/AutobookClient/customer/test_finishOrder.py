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

    def test_finish_Order(self):
        '''
        用户中心-历史订单已完成订单
        :return:
        '''
        current_activity = self.driver.current_activity
        self.driver.wait_loading()
        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()

        #点击历史订单
        personal_names = self.driver.find_ids('person_item')[1]
        personal_names.click()
        self.driver.wait_loading()
         #判断是否有已完成订单
        try:
           list_text = self.driver.find_id('tv_notice').text
           print list_text
           if u'暂无已完成历史订单' == list_text :
               pass
        except:

          #获取已完成订单列表的订单号
          order_Nos = self.driver.find_ids('order_no')
          orderNos_text = order_Nos[0].text

          #获取已完成订单列表的订单金额
          order_amounts = self.driver.find_ids('order_amount')
          amounts_text = order_amounts[0].text

          #获取已完成订单列表的订单完成时间
          order_dates = self.driver.find_ids('order_date')
          dates_text = order_dates[0].text

          #将列表取出的金额和日期转换成与数据库取出的数据格式相同
          list_info = (self.driver.to_long(amounts_text)*100,self.driver.to_datetime(dates_text))
          print list_info

          #拿列表最近一个订单号从数据库中取出该订单的金额和完成时间
          order_info = self.driver.sql('SELECT amount,insert_time FROM t_order_info a, t_order_history b WHERE a.id = b.order_info_id and a.order_no='+orderNos_text)
          print order_info

          self.assertTrue(list_info == order_info)




