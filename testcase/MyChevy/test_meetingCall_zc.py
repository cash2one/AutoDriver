__author__ = 'zhangchun'
# coding=utf-8
import unittest
from time import sleep

from framework.core import device_bak, the



#点击活动详情中的电话按钮，弹出提示框
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)


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
