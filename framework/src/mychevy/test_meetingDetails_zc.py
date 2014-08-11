# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device
from time import sleep

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_name(u'聚乐会').click()#进入最新活动页面
        sleep(2)
        els=self.driver.find_elements_by_class_name('android.widget.TextView')
        text1=els[0].text
        els[0].click()#点击第一个最新活动，进入活动详情

        self.driver.switch_to_alert()#获取弹出框
        print self.driver.current_activity#打印当前页面

        text2=self.driver.find_elements_by_class_name('android.widget.TextView')[5].text
        #print text2
        self.assertEqual(text2,text1)