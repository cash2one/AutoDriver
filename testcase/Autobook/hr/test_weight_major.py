
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




    def test_weight_null(self):
        test_weight=self.driver.find_element_by_id('detailVo_weight')
        weight=test_weight.send_keys('')
        time.sleep(1)
        self.assertTrue(test_weight.text=='',u'不存在指定字符串')
              # 体重为空



    def test_weight_long(self):
        self.driver.find_element_by_id('detailVo_weight').send_keys('1234')
        weight=self.driver.find_element_by_id('detailVo_weight').get_attribute('value')
        self.assertTrue(weight=='123',u'不存在指定字符串')
        # 体重输入超长



    def test_weight_specia(self):
        self.driver.find_element_by_id('detailVo_weight').send_keys('@##$')
        weight=self.driver.find_element_by_id('detailVo_weight').get_attribute('value')
        time.sleep(1)
        self.assertTrue(weight=='',u'不存在指定字符串')

        # 体重输入特殊字符、


    def test_weight_NaN(self):
        self.driver.find_element_by_id('detailVo_weight').send_keys('GHja@#')
        weight=self.driver.find_element_by_id('detailVo_weight').get_attribute('value')
        time.sleep(1)
        self.assertTrue(weight=='',u'不存在指定字符串')
        # 体重非数字




    def test_weight_negative(self):
        self.driver.find_element_by_id('detailVo_weight').send_keys('-234')
        weight=self.driver.find_element_by_id('detailVo_weight').get_attribute('value')
        time.sleep(1)
        self.assertTrue(weight=='234',u'不存在指定字符串')
        # 体重输入负数



    def test_weight_ture(self):
        self.driver.find_element_by_id('detailVo_weight').send_keys('66')
            # 体重输入正确的值



    def test_major_null(self):
        test_major=self.driver.find_element_by_id('detailVo_major')
        major=test_major.send_keys('')
        self.assertTrue(test_major.text=='',u'不存在指定字符串')



    def test_major_specia(self):
        self.driver.find_element_by_id('detailVo_major').send_keys('#@#$')
        major=self.driver.find_element_by_id('detailVo_major').get_attribute('value')
        time.sleep(1)
        self.assertTrue(major=='',u'不存在指定字符串')



    def test_major_letter(self):
        self.driver.find_element_by_id('detailVo_major').send_keys(u'abcde')
