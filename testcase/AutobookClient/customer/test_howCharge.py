# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'


import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):
        '''
        用户登录，查看如何收费界面
        :return:
        '''
        self.driver.wait_loading()
        #点击用户中心
        self.driver.find_id('btn_personal_center').click()
        self.driver.wait_loading()
        #查看如何收费
        self.driver.find_ids('person_item')[2].click()
        self.driver.wait_loading()

        text=self.driver.find_id('tv_title_text').text
        print text
        self.assertTrue(u'如何收费' in text,'msg')
        #点击左上角返回按钮
        self.driver.find_id('button_title_back').click()
