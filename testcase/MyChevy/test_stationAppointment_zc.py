# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#进入详情界面，点击预约保养按钮，进入预约界面
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
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000004')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(3)
        self.driver.find_element_by_name (u'详情').click()
        text1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name').text
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order')
        el.click()
        sleep(3)
        text2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_location').text
        print el.text
        self.assertEqual('.OrderActivity',self.driver.current_activity)
        self.assertEqual(text1,text2)