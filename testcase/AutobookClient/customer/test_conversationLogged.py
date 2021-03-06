# coding=utf-8

__author__ = 'wangsahnshan@126.com'


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
       '''
       用户未登录，查看实时会话界面
       :return:
       '''
       #点击进入使用
       # self.driver.find_id('start_btn').click()
       self.driver.wait_loading()
       #点击实时会话
       self.driver.find_id('rb_conversation').click()
       #去除加载
       self.driver.wait_loading()
       #判断是不是实时会话界面
       text1=self.driver.find_id('tv_title_text').text
       print text1
       self.assertTrue(u'实时会话' in text1,'msg')

       text2=self.driver.find_ids('tag_name')[0].text
       print text2
       self.assertTrue(u'当前会话' in text2,'msg')

       text3=self.driver.find_ids('tag_name')[1].text
       print text3
       self.assertTrue(u'历史会话' in text3,'msg')


