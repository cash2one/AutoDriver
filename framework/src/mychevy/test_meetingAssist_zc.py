__author__ = 'zhangchun'
# coding=utf-8
import unittest
from time import sleep
from framework.core import the,device
#点击聚乐会的最新活动，进入活动详情

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def test_case(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_name(u'聚乐会').click()
        sleep(2)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/imageView').click()
        self.driver.find_element_by_name(u'协办经销商').click()
