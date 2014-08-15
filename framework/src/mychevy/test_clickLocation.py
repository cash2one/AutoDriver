# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device
from time import sleep
#点击指定位置进入服务站查询页面
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

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
        sleep(5)
        for i in range(0,12):#以下操作连续12次
        #定位元素的原位置
            origin_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[0]
        #定位元素要移动到的目标位置
            destination_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[3]
        #执行元素的移动操作
            self.driver.drag_and_drop(origin_el,destination_el)

        self.assertEqual('.StationActivity',self.driver.current_activity)
