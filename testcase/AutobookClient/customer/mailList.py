# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    用户登录，一键下单界面点击通讯录
    '''
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       #点击一键下单按钮跳转到一键下单界面
       self.driver.find_id('rb_order').click()
       #跳转到通讯录界面
       self.driver.find_id('bt_contact').click()
       #判断该界面是否是通讯录界面
       # text=self.driver.find_id('search_src_text').text
       # print text
       #self.assertTrue(u'查找联系人' in text,'msg')

