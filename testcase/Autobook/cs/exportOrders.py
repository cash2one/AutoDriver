# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    导出文件(未完成)
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_export_open(self):
        self.driver.find_id('export').click()
        # self.driver.switch_to_alert()
        text=self.driver.find_class('xubox_dialog').text
        print text
        self.assertTrue(u'确定导出?' in text,'msg')
        time.sleep(2)
        self.driver.find_link('取消').click()
        time.sleep(10)
        # self.driver.switch_to_alert()
        # text1=self.driver.find_class('xubox_dialog').text
        # self.assertTrue(u'确定导出？' in text1,'msg')
