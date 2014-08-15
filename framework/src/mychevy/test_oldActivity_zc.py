# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device
from time import sleep
#点击点赞按钮，上下滑动列表查看点赞数是否恢复原值
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_party').click()
        sleep(3)
        self.driver.find_element_by_name(u'聚乐会活动回顾').click()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/img_partyreview').click()
        sleep(3)
        text1=self.driver.find_elements_by_class_name('android.widget.TextView')[0].text
        self.assertEqual(u'聚乐会活动回顾',text1)

