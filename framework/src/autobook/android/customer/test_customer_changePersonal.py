# coding=utf-8
__author__ = 'wangshanshan'

import time
import unittest
from framework.core import idriver_android


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer()
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):
       current_activity = self.driver.current_activity
       #点击用户中心
       self.driver.find_id('btn_personalcenter').click()

       self.driver.wait_loading()
       #点击我的信息
       self.driver.find_ids('personal_name')[0].click()
       self.driver.wait_switch()
       vali_tup = ()

       if 'true' in self.driver.find_id('personal_name').get_attribute('checked'):
           self.driver.find_id('personal_female').click()
           vali_tup += (u'女士',)


       #输入紧急联系电话
       self.driver.find_id('personal_urgent_numbers').click()
       self.driver.find_id('personal_urgent_numbers').send_keys('13636468710')

       vali_tup += ('13636468710',)

       print vali_tup

       #点击完成
       self.driver.find_id('personal_finish').click()

       #数据库中取数据
       db_array=self.driver.sql('select sex,urgency_phone from t_customer where phone=13918359985')
       #性别类型转换
       array=(self.driver.enum('sex',int(db_array[0])),db_array[1])
       print array

       #个人资料中的信息personal_female
       # text_sex = self.driver.find_id('personal_female').text
       #
       # text_urgency = self.driver.find_id('personal_urgent_numbers').text
       # text_group = (text_sex, text_urgency)
       # print text_group

       #修改性别、输入的紧急联系电话和数据库中的数据对比
       self.assertTrue(vali_tup==array,'msg')

