# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep

from framework.core import device_bak, the


#点击收藏按钮，在收藏的服务站中显示此服务站
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
        self.driver.find_element_by_name(u'详情').click()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_favorite').click()
        self.driver.back()
        sleep(3)
        #定位元素的原位置
        origin_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[0]
        #定位元素要移动到的目标位置
        destination_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[3]
        #执行元素的移动操作
        self.driver.drag_and_drop(origin_el,destination_el)
        sleep(3)
        #再次收藏服务站
        self.driver.find_elements_by_class_name('android.widget.Button')[1].click()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_favorite').click()
        self.driver.back()
        #进入收藏的服务站
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/rb_love_station').click()
        sleep(3)
        els=self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        #查看收藏的服务站是否都显示在列表中
        self.assertTrue(els[1].is_enabled())
        self.assertTrue(els[4].is_enabled())


