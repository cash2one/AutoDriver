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
     sleep(25)
        #每个测试用例，都需要把首页加入到变量mainActivity
     self.mainActivity = self.driver.current_activity

        #点击主界面的电子说明书
    def test_instructionBook_case1(self):
        #调用activity方法
        self.activity()
        #获取下标为0（第一个）的点击
        self.driver.find_elements_by_class_name('android.widget.Button')[0].click()

        #点击金领结课堂
    def test_goldBowtie_case2(self):
         #调用activity方法
        self.activity()
        #获取下标为1（第二个）的点击
        self.driver.find_elements_by_class_name('android.widget.Button')[1].click()

        #点击纯正附件
    def test_accessories_case3(self):
         #调用activity方法
        self.activity()
          #获取下标为2（第三个）的点击
        self.driver.find_elements_by_class_name('android.widget.Button')[2].click()