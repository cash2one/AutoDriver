# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
import unittest
from framework.core import idriver_android
from framework.util import str
from selenium.common import exceptions


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()
    #用户中心，历史订单-已取消订单
    def test_cancel_Order(self):
        current_activity = self.driver.current_activity
        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()


        #点击历史订单
        personal_names = self.driver.find_ids('person_item')
        personal_names[1].click()
        self.driver.wait_loading()
        #点击已取消
        self.driver.find_id('iscancle').click()
        self.driver.wait_loading()

        try :
           list_text = self.driver.find_id('tv_notice').text
           if u'暂无已取消历史订单' in list_text :
                pass
        except :

              #获取已取消订单列表的订单号
              order_Nos = self.driver.find_ids('order_no')
              orderNos_text = order_Nos[0].text


              #获取已取消订单列表的订单完成时间
              order_dates = self.driver.find_ids('order_date')
              dates_text = order_dates[0].text

              #获取已取消订单列表的订单起点
              order_from = self.driver.find_ids('order_from')
              from_text = order_from[0].text

              #将列表取出的日期转换成与数据库取出的数据格式相同
              list_info = (str.to_datetime(dates_text),from_text)
              print list_info

              #拿已取消列表最近一个订单号从数据库中取出该订单的完成时间和起点
              order_info = self.driver.sql('SELECT insert_time,start_address FROM t_order_info a, t_order_history b WHERE a.id = b.order_info_id and a.order_no='+orderNos_text)
              print order_info

              self.assertTrue(list_info == order_info)