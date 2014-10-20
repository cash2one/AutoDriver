# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device_bak
from time import sleep
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
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        sleep(5)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('zzzz')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000001')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(5)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_cancel').click()
        #登录失败
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_party').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/imageView').click()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/content_apply').click()
        self.driver.switch_to_alert()
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_msg')
        txt=el.text
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_cancel').click()
        self.assertTrue(u'登录失败：用户信息不正确' in txt)
        self.assertFalse(el.is_displayed())