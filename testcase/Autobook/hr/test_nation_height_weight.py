# coding=utf-8
__author__ = 'lvfangying@pathbook.com.cn'

#hr_循环验证用户名错误登录测试

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()



    def test_nation(self):
        self.driver.find_element_by_id('btn_add').click()
        test_nation_tx=self.driver.find_element_by_id('detailVo_nation_tip').text
        self.assertTrue(u'民族不能为空.'in test_nation_tx)


    # def test_driverVo_phone(self,driverVo_phone):
    #     self.driver.find_element_by_id('driverVo_phone').send_keys(driverVo_phone)

    def test_nation_null(self):
        driverVo_phone=self.driver.find_element_by_id('driverVo_phone')
        aa=driverVo_phone.send_keys('')
        print aa
        time.sleep(1)
        self.assertTrue(driverVo_phone.text=='',u'不存在指定字符串')
        # 本人联系电话为空


    def test_phone_long(self):
        driverVo_phone=self.driver.find_element_by_id('driverVo_phone')
        driverVo_phone.send_keys('156186334121')
        phone=self.driver.find_element_by_id('driverVo_phone').get_attribute('value')
        time.sleep(1)
        self.assertTrue(phone=='15618633412',u'不存在指定字符串')
        # 本人联系电话输入超长


    def test_phone_specia(self):
        driverVo_phone=self.driver.find_element_by_id('driverVo_phone')
        driverVo_phone.send_keys('@#$')
        phone=self.driver.find_element_by_id('driverVo_phone').get_attribute('value')
        time.sleep(1)
        self.assertTrue(driverVo_phone.text=='',u'不存在指定字符串')
        # 本人联系电话输入特殊字符


    def test_phone_j(self):
        driverVo_phone=self.driver.find_element_by_id('driverVo_phone')
        driverVo_phone.send_keys('jjgh')
        phone=self.driver.find_element_by_id('driverVo_phone').get_attribute('value')
        time.sleep(1)
        self.assertTrue(driverVo_phone.text=='',u'不存在指定字符串')
        # 本人联系电话输入大小写字母


    def test_phone_ture(self):
        self.driver.find_element_by_id('driverVo_phone').send_keys('15618633412')
       # 输入正确的本人联系电话