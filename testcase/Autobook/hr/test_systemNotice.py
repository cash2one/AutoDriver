# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_setting_reset(self):
       #点击系统公告
       self.driver.find_element_by_id('sysNotice').click()
       nametx=self.driver.find_element_by_id('sysNotice').text
       self.assertTrue(u'系统公告' in nametx)
       #点击未读
       self.driver.find_element_by_id('unRead').click()
       untx=self.driver.find_element_by_id('unRead').text
       self.assertTrue(u'未读' in untx)
       contx=self.driver.find_element_by_id('content').text
       if contx==u"没有数据哦╮(╯_╰)╭":
          print '没有信息'
       else :
          print contx
