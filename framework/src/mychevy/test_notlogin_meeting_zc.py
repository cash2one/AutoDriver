__author__ = 'zhangchun'
# coding=utf-8
import unittest
from time import sleep
from framework.core import the,device


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

        els=self.driver.find_elements_by_class_name('android.widget.TextView')
        els[0].click()
        sleep(2)

        self.driver.find_elements_by_class_name('android.widget.Button')[1].click()#未登录点击报名进入登录页面
        self.driver.switch_to_alert()

        print(self.driver.current_activity)
        self.assertEqual('.UserInformationActivity',self.driver.current_activity)

