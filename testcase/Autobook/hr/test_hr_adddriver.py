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

    # def test_driver_name(self,driver_name):
    #     self.testValue()
    #     self.driver.find_element_by_id('driverVo_name').send_keys(driver_name)


    def test_name0(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_name_tx=self.driver.find_element_by_id('driverVo_name_tip').text
        self.assertTrue(u'姓名不能为空.'in driverVo_name_tx)
        # driverVo_sfz_tx=self.driver.find_element_by_id('driverVo_card_tip').text
        # self.assertTrue(u'身份证号不能为空.'in driverVo_sfz_tx)


    # def test_name1(self,driver_name):
    #     self.driver.find_element_by_id('driverVo_name').send_keys(driver_name)
        # self.driver.find_element_by_id('btn_add').click()

    def test_name_null(self):
        driver_name=self.driver.find_element_by_id('driver_name')
        driver_name.send_kets('')
        time.sleep(1)
        self.assertTrue(driver_name.text=='','')
        # 姓名为空


    def test_name_long(self):
        driver_name=self.driver.find_element_by_id('driver_name')
        driver_name.send_kets('赵茜阿尔木子克里斯蒂娜')
        time.sleep(1)
        self.assertTrue(driver_name.text=='赵茜阿尔木子','')
        # 姓名输入超长


    def test_name_num(self):
        driver_name=self.driver.find_element_by_id('driver_name')
        driver_name.send_kets('54351')
        time.sleep(1)
        self.assertTrue(driver_name.text=='','')
        # 姓名输入数字

    def test_name_special(self):
        driver_name=self.driver.find_element_by_id('driver_name')
        driver_name.send_kets('%%￥￥')
        time.sleep(1)
        self.assertTrue(driver_name.text=='','')
        # 姓名输入特殊字符

    def test_name(self):
        self.driver.find_element_by_id('driver_name').send_keys(u'陈快乐')
         # 姓名输入正确的值



    def test_sex0(self):
        self.test_name0()
        # self.driver.find_element_by_id('bth_add').click()
        driverVo_sex=self.driver.find_element_by_id('driverVo_sex_tip').text
        self.assertTrue(u'请选择性别.'in driverVo_sex)


    def test_sex1(self):
        sexs=self.driver.find_element_by_id('driverVo_sex').find_elements_by_tag_name('option')
        # time.sleep(1)
        for sex in sexs:
            if sex.get_attribute('value')=='0':
                sex.click()
                self.assertTrue(sex.is_selected())

    def test_sex2(self):
        sexs=self.driver.find_element_by_id('driverVo_sex').find_elements_by_tag_name('option')
        # time.sleep(1)
        for sex in sexs:
            if sex.get_attribute('value')=='1':
                sex.click()
                self.assertTrue(sex.is_selected())

    def test_marriage0(self):
        self.test_name0()
        # self.driver.find_element_by_id('bth_add').click()
        driverVo_marriage=self.driver.find_element_by_id('detailVo_marriage_tip').text
        self.assertTrue(u'请选择婚育.'in driverVo_marriage)


    def test_marriage1(self):
        marriages=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        # time.sleep(1)
        for marriage in marriages:
            if marriage.get_attribute('value')=='0':
                marriage.click()
                self.assertTrue(marriage.is_selected())


    def test_marriage2(self):
        marriages=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        # time.sleep(1)
        for marriage in marriages:
            if marriage.get_attribute('value')=='1':
                marriage.click()
                self.assertTrue(marriage.is_selected())










