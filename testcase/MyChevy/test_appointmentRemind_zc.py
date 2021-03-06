# coding=utf-8
__author__ = 'zhangchun'

import time
from drivers import *

#点击预约保养，点击提示框的确定按钮，成功预约
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        time.sleep(5)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000002')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        time.sleep(10)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        time.sleep(10)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_location').click()
        time.sleep(5)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name').click()
        #选择指定位置

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').click()
        self.driver.switch_to_alert()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[4].click()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        time.sleep(3)
        #选择期望时间

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        self.driver.switch_to_alert()
        time.sleep(3)
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_msg')
        txt=el.text
        #print txt
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_cancel').click()

        self.assertTrue(u'在上海强生北美汽车销售服务有限公司申请预约保养?' in txt)
        self.assertFalse(el.is_displayed())
