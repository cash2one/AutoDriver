# coding=utf-8
__author__ = 'gaoxu'
import unittest
from time import sleep
from framework.core import the,device

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver=device.android()

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def activity(self):
        sleep(10)
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
    def test_case1(self):
        self.activity()
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton1').click()
        sleep(0.5)
# #点击右侧翻按钮
    def test_case2(self):
        self.activity()
        self.test_case1()
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton_direction_arrow_r').click()
        sleep(0.5)
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton_direction_arrow_r').click()
        sleep(0.5)
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton_direction_arrow_r').click()
        sleep(0.5)
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton_direction_arrow_r').click()

#点击左右侧翻按钮
    def test_case3(self):
        self.activity()
        self.test_case1()
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton_direction_arrow_r').click()
        sleep(0.5)
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton_direction_arrow_l').click()
        sleep(0.5)
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton_direction_arrow_r').click()