# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *


#点击聚乐会的最新活动，进入活动详情

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_name(u'聚乐会').click()
        sleep(2)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/imageView').click()
        self.driver.find_element_by_name(u'协办经销商').click()
