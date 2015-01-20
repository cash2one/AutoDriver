# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#点击活动详情中的电话按钮，弹出提示框
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
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/imageView').click()
        sleep(2)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/content_phone').click()
        #点击拨打电话按钮，获取提示框
        self.driver.switch_to_alert()
        sleep(2)
        txt=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_msg').text

        print txt#打印提示内容
        self.assertEqual(u'没有找到蓝牙设备，请检查蓝牙连接是否正确',txt)
