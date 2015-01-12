# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep

from framework.core import device_bak, the


#点击收藏按钮，在收藏的服务站中显示此服务站
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(3)
        self.driver.find_element_by_name(u'详情').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_favorite').click()
        #点击收藏按钮
        device_bak.switchToHome(self,self.mainActivity)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/rb_love_station').click()
        #点击收藏的服务站
        sleep(3)
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/ll_hour24_list_row')
        self.assertTrue(el.is_enabled())#收藏的服务站列表中显示该服务站