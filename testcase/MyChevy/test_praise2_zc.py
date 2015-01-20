#coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#点击详情，点击赞按钮，查看点赞数
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(3)
        self.driver.find_element_by_name(u'详情').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_ok').click()
        txt1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_ok_number').text
        self.driver.back()
        txt2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_ok_number').text
        self.assertEqual(txt1,txt2)

