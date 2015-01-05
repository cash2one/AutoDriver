# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep

from framework.core import device_bak
from framework.data import the

#点击点赞按钮，上下滑动列表查看点赞数是否恢复原值
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(5)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_ok').click()
        #点击点赞图标
        text1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_ok_number').text
        sleep(3)
        for i in range(0,12):#以下操作连续12次
        #定位元素的原位置
            origin_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[0]
        #定位元素要移动到的目标位置
            destination_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[3]
            self.driver.drag_and_drop(origin_el,destination_el)
        #执行元素的移动操作
        sleep(3)
        for i in range(0,12):#以下操作连续12次
        #定位元素的原位置
            origin_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[3]
        #定位元素要移动到的目标位置
            destination_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[0]
            self.driver.drag_and_drop(origin_el,destination_el)
        text2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_ok_number').text
        self.assertEqual(text1,text2)