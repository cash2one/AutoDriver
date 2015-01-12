# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep

from framework.core import device_bak, the


#点击查看详情，进入对应页面
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

        sleep(2)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000002')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(5)
        txt= self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_notify_message').text
        i=txt[5]  #循环的次数，即提示的个数

        for n in range(0,int(i)):
            txt= self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_notify_message').text
            self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_notify_detail').click()
            sleep(2)
            t1=txt[-4:]
            #取提示内容最后4个字符
            if t1==u'保养预约':#最后4个为保养预约，则进入预约的详情界面
                txt1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name').text
                self.assertTrue(txt1 in txt)#详情中的标题与提示信息中的是否一致
            else:#否则，进入报名活动的详情界面
                txt2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/name').text
                self.assertTrue(txt2 in txt)
            self.driver.back()#返回上一页
            sleep(5)