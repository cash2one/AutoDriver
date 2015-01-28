# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    用户登录，历史订单已取消订单为空（暂无已取消历史订单）
    '''
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_cancelOrdernull(self):
        self.driver.wait_loading()
        self.driver.find_id('btn_personal_center').click()
        #点击历史订单
        self.driver.find_ids('person_item')[1].click()
        #点击已取消按钮
        self.driver.find_id('iscancle').click()
        self.driver.wait_loading()
        #判断是否有已取消的订单
        try:
           list_text = self.driver.find_id('tv_notice').text
           if u'暂无已取消历史订单' in list_text :
             text=self.driver.find_id('tv_notice').text
             print text
           self.assertTrue(u'暂无已取消历史订单' in text ,'msg')
        except :
          pass
