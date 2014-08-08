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
        self.driver.find_elements_by_class_name('android.widget.Button')[0].click()
#点击左侧翻按钮
    def test_leftButton_case1(self):
        self.activity()
        self.test_case1()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
#点击右侧翻按钮
    def test_rightButton_case2(self):
        self.activity()
        self.test_case1()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[3].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[3].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[3].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[3].click()
#点击右侧翻按钮
    def test_leftRightButton_case3(self):
        self.activity()
        self.test_case1()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[3].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[3].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()