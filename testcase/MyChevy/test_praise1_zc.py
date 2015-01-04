# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device_bak
from time import sleep
#点击点赞图标，点赞数加1
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
        txt1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_ok_number').text
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_ok').click()
        sleep(3)
        txt2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_ok_number').text
        print txt2
        print txt1