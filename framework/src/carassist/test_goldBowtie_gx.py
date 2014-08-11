# coding=utf-8
__author__ = 'gaoxu'
import unittest
from time import sleep
from framework.core import the,device


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.android()

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def activity(self):
     sleep(15)
        #每个测试用例，都需要把首页加入到变量mainActivity
     self.mainActivity = self.driver.current_activity
 #点击金领结课堂
    def test_case1(self):
         #调用activity方法
        self.activity()
        #获取id并点击
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton2').click()