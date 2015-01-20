
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


    def test_card(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_card_tx=self.driver.find_element_by_id('driverVo_card_tip').text
        self.assertTrue(u'身份证号不能为空.'in driverVo_card_tx)

    # def test_card1(self,driver_card):
    #     self.driver.find_element_by_id('driverVo_card').send_keys(driver_card)


    def test_card_long(self):
        driver_card=self.driver.find_element_by_id('driver_card')
        driver_card.send_keys('4305231993020241402')
        time.sleep(1)

        self.assertTrue(driver_card.text=='430523199302024140','')
        # 身份证超长


    def test_card_special(self):
        driver_card=self.driver.find_element_by_id('driver_card')
        driver_card.send_keys('#$$')
        time.sleep(1)
        self.assertTrue(driver_card.text=='','')
        # 身份证为特殊字符


    def test_card_j(self):
        driver_card=self.driver.find_element_by_id('driver_card')
        driver_card.send_keys('hhdr')
        time.sleep(1)
        self.assertTrue(driver_card.text=='','')
        # 身份证最后一位为大小写字母


    def test_card_Non_capital_letters(self):
        driver_card=self.driver.find_element_by_id('driver_card')
        driver_card.send_keys('43052319930202414x')
        time.sleep(1)
        self.assertTrue(driver_card.text=='43052319930202414','')
        # 身份证最后一位为小写字母x


    def test_card_ture(self):
        self.driver.find_element_by_id('driver_card').send_keys('430523199302024140')
        # 正确的身份证号


    def test_licenseNo(self):
        self.driver.find_element_by_id("btn_add").click()
        test_licenseNo_tx=self.driver.find_element_by_id('detailVo_licenseNo_tip').text
        self.assertTrue(u'驾照档案编号不能为空.'in test_licenseNo_tx)


    # def test_detailVo_licenseNo(self,detailVo_licenseNo):
    #     self.driver.find_element_by_id('detailVo_licenseNo').send_keys(detailVo_licenseNo)

    def test__licenseNo_null(self):
        detailVo_licenseNo=self.driver.find_element_by_id('detailVo_licenseNo')
        detailVo_licenseNo.send_keys('')
        time.sleep(1)
        self.assertTrue(detailVo_licenseNo.text=='',u'')
        # 驾照档案编号为空


    def test_licenseNo_long(self):
        detailVo_licenseNo=self.driver.find_element_by_id('detailVo_licenseNo')
        detailVo_licenseNo.send_keys('22222222222222122233')
        time.sleep(1)
        self.assertTrue(detailVo_licenseNo.text=='222222222222221222',u'')
        # 驾照档案编号输入超长


    def test_phone_special(self):
        detailVo_licenseNo=self.driver.find_element_by_id('detailVo_licenseNo')
        detailVo_licenseNo.send_keys('@￥#￥')
        time.sleep(1)
        self.assertTrue(detailVo_licenseNo.text=='',u'文本框输入特殊字符不成立')
        # 驾照档案编号输入特殊字符


    def test_licenseNo_j(self):
        detailVo_licenseNo=self.driver.find_element_by_id('detailVo_licenseNo')
        detailVo_licenseNo.send_keys('hIO')
        time.sleep(1)
        self.assertTrue(detailVo_licenseNo.text=='',u'')
        # 驾照档案编号输入大小写字母

    def test_licenseNo_ture(self):
        self.driver.find_element_by_id('detailVo_licenseNo').send_keys('10000101')
        # 输入正确的驾照档案编号



    def test_phone(self):
        self.driver.find_element_by_id('btn_add').click()
        test_phone_tx=self.driver.find_element_by_id('driverVo_phone_tip').text
        self.assertTrue(u'本人联系电话不能为空.'in test_phone_tx)


    # def test_driverVo_phone(self,driverVo_phone):
    #     self.driver.find_element_by_id('driverVo_phone').send_keys(driverVo_phone)

    def test__phone_null(self):
        driverVo_phone=self.driver.find_element_by_id('driverVo_phone')
        driverVo_phone.send_keys('')
        time.sleep(1)
        self.assertTrue(driverVo_phone.text=='',u'')
        # 本人联系电话为空


    def test_phone_long(self):
        driverVo_phone=self.driver.find_element_by_id('driverVo_phone')
        driverVo_phone.send_keys('156186334121')
        time.sleep(1)
        self.assertTrue(driverVo_phone.text=='15618633412',u'')
        # 本人联系电话输入超长


    def test_phone_specia(self):
        driverVo_phone=self.driver.find_element_by_id('driverVo_phone')
        driverVo_phone.send_keys('@#$')
        time.sleep(1)
        self.assertTrue(driverVo_phone.text=='',u'')
        # 本人联系电话输入特殊字符


    def test_phone_j(self):
        driverVo_phone=self.driver.find_element_by_id('driverVo_phone')
        driverVo_phone.send_keys('jjgh')
        time.sleep(1)
        self.assertTrue(driverVo_phone.text=='',u'')
        # 本人联系电话输入大小写字母


    def test_phone_ture(self):
        self.driver.find_element_by_id('driverVo_phone').send_keys('15618633412')
       # 输入正确的本人联系电话
