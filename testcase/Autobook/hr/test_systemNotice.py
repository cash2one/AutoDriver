# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()
        # 关闭浏览器
        # self.driver.close()

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
          notx=self.driver.find_element_by_class_name('notice_row').text
          self.assertTrue(u'1、' in notx)
          self.driver.find_element_by_class_name('notice_row').click()


    def test_setting_readed(self):

       #点击系统公告
       self.driver.find_element_by_id('sysNotice').click()
       nametx=self.driver.find_element_by_id('sysNotice').text
       self.assertTrue(u'系统公告' in nametx)
       #点击未读
       self.driver.find_element_by_id('readed').click()
       untx=self.driver.find_element_by_id('readed').text
       self.assertTrue(u'已读' in untx)
       contx=self.driver.find_element_by_id('content').text
       if contx==u"没有数据哦╮(╯_╰)╭":
          print '没有信息'
       else :
          print contx
          notx=self.driver.find_element_by_class_name('notice_row').text
          self.assertTrue(u'1、' in notx)
          self.driver.find_element_by_class_name('notice_row').click()

