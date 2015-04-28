
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



    def test_drivingAge(self):
        self.driver.find_element_by_id('btn_add').click()
        drivingAge_tx=self.driver.find_element_by_id('driverVo_drivingAge_tip').text
        self.assertTrue(u'驾龄不能为空.'in drivingAge_tx)



    def test_drivingAge_null(self):
        drivingAge=self.driver.find_element_by_id('driverVo_drivingAge')
        drivingAge.send_keys('')
        time.sleep(1)
        self.assertTrue(drivingAge.text=='',u'不存在指定字符串')
        # 驾龄为空


    def test_drivingAge_long(self):
        self.driver.find_element_by_id('driverVo_drivingAge').send_keys('100')
        drivingAge=self.driver.find_element_by_id('driverVo_drivingAge').get_attribute('value')
        time.sleep(1)
        self.assertTrue(drivingAge=='10',u'不存在指定字符串')
        # 驾龄超长


    def test_drivingAge_special(self):
        self.driver.find_element_by_id('driverVo_drivingAge').send_keys(u'#$$')
        drivingAge=self.driver.find_element_by_id('driverVo_drivingAge').get_attribute('value')
        time.sleep(1)
        self.assertTrue(drivingAge=='',u'不存在指定字符串')
        # 驾龄输入特殊字符


    def test_drivingAge_nan(self):
        self.driver.find_element_by_id('driverVo_drivingAge').send_keys(u'三十')
        drivingAge=self.driver.find_element_by_id('driverVo_drivingAge').get_attribute('value')
        time.sleep(1)
        self.assertTrue(drivingAge=='',u'不存在指定字符串')
        # 驾龄输入非数字


    def test_drivingAge_ture(self):
        self.driver.find_element_by_id('driverVo_drivingAge').send_keys('10')
        # 输入正确的驾龄




    def test_urgencyName(self):
        self.driver.find_element_by_id('btn_add').click()
        urgencyName_tx=self.driver.find_element_by_id('detailVo_urgencyName_tip').text
        self.assertTrue(u'紧急联系人姓名不能为空.'in urgencyName_tx)



    def test_urgencyName_null(self):
        self.driver.find_element_by_id('detailVo_urgencyName').send_keys('')
        urgencyName=self.driver.find_element_by_id('detailVo_urgencyName').get_attribute('value')
        time.sleep(1)
        self.assertTrue(urgencyName=='',u'不存在指定字符串')
        # 紧急联系人姓名为空


    def test_urgencyName_special(self):
        self.driver.find_element_by_id('detailVo_urgencyName').send_keys('@$$#')
        urgencyName=self.driver.find_element_by_id('detailVo_urgencyName').get_attribute('value')
        time.sleep(1)
        self.assertTrue(urgencyName=='',u'不存在指定字符串')
        # 紧急联系人姓名输入特殊字符



    def test_urgencyName_num(self):
        self.driver.find_element_by_id('detailVo_urgencyName').send_keys('123')
        urgencyName=self.driver.find_element_by_id('detailVo_urgencyName').get_attribute('value')
        time.sleep(1)
        self.assertTrue(urgencyName=='',u'不存在指定字符串')
        # 紧急联系人姓名输入数字


    def test_urgencyName_ture(self):
        self.driver.find_element_by_id('detailVo_urgencyName').send_keys(u'张三')
        # 输入正确的紧急联系人姓名




    def test_urgencyTel(self):
        self.driver.find_element_by_id('btn_add').click()
        urgencyTel_tx=self.driver.find_element_by_id('detailVo_urgencyTel_tip').text
        self.assertTrue(u'电话不能为空.'in urgencyTel_tx)



    def test_urgencyTel_null(self):
        self.driver.find_element_by_id('detailVo_urgencyTel').send_keys('')
        urgencyTel=self.driver.find_element_by_id('detailVo_urgencyTel').get_attribute('value')
        time.sleep(1)
        self.assertTrue(urgencyTel=='',u'不存在指定字符串')
        # 电话为空


    def test_urgencyTel_special(self):
        self.driver.find_element_by_id('detailVo_urgencyTel').send_keys('@$$#')
        urgencyTel=self.driver.find_element_by_id('detailVo_urgencyTel').get_attribute('value')
        time.sleep(1)
        self.assertTrue(urgencyTel=='',u'不存在指定字符串')
        # 电话输入特殊字符



    def test_urgencyTel_nun(self):
        self.driver.find_element_by_id('detailVo_urgencyTel').send_keys(u'一二好')
        urgencyTel=self.driver.find_element_by_id('detailVo_urgencyTel').get_attribute('value')
        time.sleep(1)
        self.assertTrue(urgencyTel=='',u'不存在指定字符串')
        # 电话输入非数字



    def test_urgencyTel_long(self):
        self.driver.find_element_by_id('detailVo_urgencyTel').send_keys('136016775495')
        urgencyTel=self.driver.find_element_by_id('detailVo_urgencyTel').get_attribute('value')
        time.sleep(1)
        self.assertTrue(urgencyTel=='13601677549',u'不存在指定字符串')
        # 电话输入超长



    def test_urgencyTel_ture(self):
        self.driver.find_element_by_id('detailVo_urgencyTel').send_keys('13601677549')
        # 输入正确的电话号码