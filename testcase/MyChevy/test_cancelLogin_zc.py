# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *


#输入不存在的用户登录后，弹出提示框
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        sleep(5)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_cancel').click()
        #print(self.driver.current_activity)
        self.assertEqual('.MainActivity',self.driver.current_activity)
