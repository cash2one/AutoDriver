# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

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
        self.driver.switch_to_alert()#获取弹出框
        #print(self.driver.current_activity)
        self.assertEqual('.NewPartyActivity',self.driver.current_activity)
