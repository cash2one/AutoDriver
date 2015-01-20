# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#点击24小时服务站后，点击收藏的服务站
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
        sleep(4)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/rb_love_station').click()
        txt=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_love_empty').text
        self.assertEqual(u'目前还没有收藏的服务站',txt)