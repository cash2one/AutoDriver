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
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        sleep(5)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').clear()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('hdfuo')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').clear()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000002')
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()

        self.driver.switch_to_alert()
        print self.driver.current_activity
        self.assertEqual('.OrderActivity',self.driver.current_activity)
