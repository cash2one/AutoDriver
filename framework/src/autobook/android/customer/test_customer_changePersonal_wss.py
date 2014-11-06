# coding=utf-8

__author__ = 'Administrator'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.customer')
        idriver.login_customer(self.driver)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):
       current_activity = self.driver.current_activity
       #点击用户中心
       self.driver.find_id('btn_personalcenter').click()
       #点击我的信息
       self.driver.find_id('personal_name').click()
       #选择女士
       self.driver.find_id('personal_female').click()
        #pkg = self.driver.package
       # 选择性别
       # if 'true' not in self.driver.find_element_by_id(pkg+'personal_female').get_attribute('checked'):
       #   self.driver.find_id('personal_female').click()
       #输入紧急联系电话
       self.driver.find_id('personal_urgent_numbers').click()
       self.driver.find_id('personal_urgent_numbers').send_keys('13636468710')


       #点击完成
       self.driver.find_id('personal_finish').click()

       #数据库中取数据
       db_array=self.driver.sql('select sex,urgency_phone from t_customer where phone=13918359985')
       #性别类型转换
       print db_array
       array=(idriver.sex(int(db_array[0])),db_array[1])
       print array

       #个人资料中的信息
       text_sex=self.driver.find_id('personal_female').get_attribute('text')


       text_urgency=self.driver.find_id('personal_urgent_numbers').text
       text_group=(text_sex,text_urgency)
       print text_group

       #修改性别、输入的紧急联系电话和数据库中的数据对比
       self.assertTrue(text_group==array,'msg')

