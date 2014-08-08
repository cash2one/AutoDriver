__author__ = 'zhangchun'
# coding=utf-8
import unittest
from time import sleep
from framework.core import the,device


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android()

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)


    def test_case(self):
        #每个测试用例，都需要把首页加入到变量mainActivity

        self.mainActivity = self.driver.current_activity
        els=self.driver.find_elements_by_class_name('android.widget.ImageView')
        els[3].click()
        sleep(2)
        self.driver.switch_to_alert()
        self.assertEqual('.UserInformationActivity',self.driver.current_activity)