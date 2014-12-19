# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
#上下滑动已完取消单列表，提示“无数据可加载”(还未完成)
import time
import unittest
from framework.core import idriver_android
from selenium.common import exceptions



class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_cancel_order(self):

        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()
        #点击历史订单
        self.driver.find_ids('person_item')[1].click()
        self.driver.wait_loading()

        #点击已取消
        self.driver.find_id('iscancle').click()
        self.driver.wait_loading()

        try:
           list_text = self.driver.find_id('tv_notice').text
           if u'暂无已取消历史订单' in list_text :
             pass
        except:

         #获取所有已完成订单列表的订单号
         order = self.driver.swipe_load_item('lv_finish','order_finish_item','order_no',page_size=10)






