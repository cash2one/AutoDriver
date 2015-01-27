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
        driverVo_phone=self.driver.find_element_by_id('detailVo_nation')
        nation=driverVo_phone.send_keys('')
        time.sleep(1)
        self.assertTrue(driverVo_phone.text=='',u'不存在指定字符串')
        # 民族为空


    # def test_nation_long(self):
    #     self.driver.find_element_by_id('detailVo_nation').send_keys(u'汉族的就是唱得好都或多或少大概结果就看过快乐')
    #     nation=self.driver.find_element_by_id('detailVo_nation').get_attribute('value')
    #     time.sleep(1)
    #     self.assertTrue(nation==u'汉族的就是唱得好都或多或少大概结果就看过',u'不存在指定字符串')
    #     # 民族输入超长


    def test_nation_specia(self):
        self.driver.find_element_by_id('detailVo_nation').send_keys(u'@#$')
        nation=self.driver.find_element_by_id('detailVo_nation').get_attribute('value')
        time.sleep(1)
        self.assertTrue(nation=='',u'不存在指定字符串')
        # 民族输入特殊字符


    def test_nation_j(self):
        self.driver.find_element_by_id('detailVo_nation').send_keys(u'jjgh')
        nation=self.driver.find_element_by_id('detailVo_nation').get_attribute('value')
        time.sleep(1)
        self.assertTrue(nation=='jjgh',u'不存在指定字符串')
        # 民族输入大小写字母


    def test_nation_ture(self):
        self.driver.find_element_by_id('detailVo_nation').send_keys(u'汉族')
       # 输入正确的民族