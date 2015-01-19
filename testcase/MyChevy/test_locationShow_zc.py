# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *


#点击指定位置进入服务站查询页面
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
        sleep(2)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000002')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        sleep(5)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_location').click()
        sleep(3)
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name')
        text1=el.text
        el.click()
        text2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_location').text
        self.assertEqual(text1,text2)