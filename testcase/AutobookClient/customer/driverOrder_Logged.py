# coding=utf-8
__author__ = 'wangsahnshan@126.com'
#用户未登录，指定司机下单（周边有司机）

import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        #self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       current_activity = self.driver.current_activity
       #点击进入使用
       # self.driver.find_id('start_btn').click()
       self.driver.wait_loading()

       #点击附近司机列表
       self.driver.find_id('rb_map_list').click()
       self.driver.wait_loading()
       #判断列表中是否有司机
       nearbyrivers = []
       try:
          nearbyrivers = self.driver.find_ids('nearbyriver')
       except self.driver.NoSuchElementException:
            pass

       self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')

       driver_exist = False

       for d in nearbyrivers:
           d_name = d.find_element_by_id(self.driver.pkg+'big_name').text
           self.driver.swipe(0,0,0,100,0.8)

           print d_name
           if u'康小伟' in d_name:
               driver_exist = True
               d.click()
               self.driver.wait_switch('.MainActivity')

               # 点击立即下单
               self.driver.find_id('driver_order').click()
               self.driver.wait_loading()


               break

       #跳转到填写手机号界面
       txt=self.driver.find_id('tv_title_text').text
       print txt
       self.assertTrue(u'填写手机号' in txt,'msg')







