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


    def test_detailVo_licenseNum(self):
        self.driver.find_element_by_id('btn_add').click()
        test_licenseNum_tx=self.driver.find_element_by_id('detailVo_licenseNum_tip').text
        self.assertTrue(u'驾驶证号码不能为空.'in test_licenseNum_tx)

    # def  test_licenseNum1(self,detailVo_licenseNum):
    #     self.driver.find_element_by_id('detailVo_licenseNum').send_keys(detailVo_licenseNum)

    def test__licenseNum_null(self):
        detailVo_licenseNum=self.driver.find_element_by_id('detailVo_licenseNum')
        detailVo_licenseNum.send_keys('')
        time.sleep(1)
        self.assertTrue(detailVo_licenseNum.text=='','')
        # 驾驶证号码为空


    def test_licenseNum_long(self):
        detailVo_licenseNum=self.driver.find_element_by_id('detailVo_licenseNum')
        detailVo_licenseNum.send_keys('4305231993020241402')
        time.sleep(1)
        self.assertTrue(detailVo_licenseNum.text=='430523199302024140','')
        # 驾驶证号码输入超长


    def test_licenseNum_special(self):
        detailVo_licenseNum=self.driver.find_element_by_id('detailVo_licenseNum')
        detailVo_licenseNum.send_keys('@$@')
        time.sleep(1)
        self.assertTrue(detailVo_licenseNum.text=='','')
        # 驾驶证号码输入特殊字符


    def test_licenseNum_j(self):
        detailVo_licenseNum=self.driver.find_element_by_id('detailVo_licenseNum')
        detailVo_licenseNum.send_keys('hghf')
        time.sleep(1)
        self.assertTrue(detailVo_licenseNum.text=='','')
        # 驾驶证号码输入大小写字母


    def test_licenseNum_ture(self):
        self.driver.find_element_by_id('detailVo_licenseNum').send_keys('430523199302024140')
        # 输入正确的驾驶证号码.


    def test_imsi(self):
        self.driver.find_element_by_id('btn_add').click()
        test_imsi_tx=self.driver.find_element_by_id('driverVo_imsi_tip').text
        self.assertTrue(u'手机标识号不能为空.'in test_imsi_tx)


    # def test_driverVo_phone(self,driverVo_phone):
    #     self.driver.find_element_by_id('driverVo_phone').send_keys(driverVo_phone)

    def test_imsi_null(self):
        driverVo_imsi=self.driver.find_element_by_id('driverVo_imsi')
        driverVo_imsi.send_keys('')
        time.sleep(1)
        self.assertTrue(driverVo_imsi.text=='',u'')
        # 手机标识号为空


    def test_imsi_long(self):
        driverVo_imsi=self.driver.find_element_by_id('driverVo_imsi')
        driverVo_imsi.send_keys('46002701738556865')
        time.sleep(1)
        self.assertTrue(driverVo_imsi.text=='460027017385568',u'')
        # 手机标识号输入超长


    def test_imsi_specia(self):
        driverVo_imsi=self.driver.find_element_by_id('driverVo_phone')
        driverVo_imsi.send_keys('@#$')
        time.sleep(1)
        self.assertTrue(driverVo_imsi.text=='',u'')
        #  手机标识号输入特殊字符


    def test_imsi_j(self):
        driverVo_imsi=self.driver.find_element_by_id('driverVo_imsi')
        driverVo_imsi.send_keys('jjgh')
        time.sleep(1)
        self.assertTrue(driverVo_imsi.text=='',u'')
        # 手机标识号输入大小写字母


    def test_imsi_ture(self):
        self.driver.find_element_by_id('driverVo_imsi').send_keys('15618633412')
       # 输入正确的手机标识号





