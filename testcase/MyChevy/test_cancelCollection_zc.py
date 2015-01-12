# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep

from framework.core import device_bak, the


#点击取消收藏，服务站在收藏的服务站列表中消失
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        # self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        # sleep(3)
        # self.driver.find_element_by_name(u'详情').click()
        # sleep(3)
        # self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_favorite').click()
        # # #点击收藏按钮
        # device.switchToHome(self,self.mainActivity)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(5)
        self.driver.find_element_by_name(u'详情').click()
        sleep(5)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_favorite').click()
        self.driver.back()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/rb_love_station').click()
        txt=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_love_empty').text
        self.assertFalse(u'上海强生北美汽车销售服务有限公司' in txt)

