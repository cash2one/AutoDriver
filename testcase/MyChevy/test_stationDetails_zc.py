# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep

from framework.core import device_bak, the


#点击收藏按钮，在预约保养的收藏的服务站中显示此服务站
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(3)
        self.driver.find_element_by_name(u'详情').click()
        sleep(3)
        #print(self.driver.current_activity)
        self.assertEqual('.StationDetailActivity',self.driver.current_activity)
