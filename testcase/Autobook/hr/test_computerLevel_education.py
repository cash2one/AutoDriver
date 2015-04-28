
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





    def test_computerLevel(self):
        computerLevels=self.driver.find_element_by_id('detailVo_computerLevel').find_elements_by_tag_name('option')
        # time.sleep(1)
        for computerLevel in computerLevels:
            if computerLevel.get_attribute('value')=='-99':
                computerLevel.click()
                self.assertTrue(computerLevel.is_selected())




    def test_computerLevel_one(self):
        computerLevels=self.driver.find_element_by_id('detailVo_computerLevel').find_elements_by_tag_name('option')
        # time.sleep(1)
        for computerLevel in computerLevels:
            if computerLevel.get_attribute('value')=='1':
                computerLevel.click()
                self.assertTrue(computerLevel.is_selected())



    def test_education(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_education_tx=self.driver.find_element_by_id('detailVo_education_tip').text
        self.assertTrue(u'请选择学历.'in driverVo_education_tx)


    def test_education_value(self):
        educations=self.driver.find_element_by_id('detailVo_education').find_elements_by_tag_name('option')
        # time.sleep(1)
        for education in educations:
            if education.get_attribute('value')=='-99':
                education.click()
                self.assertTrue(education.is_selected())




    def test_education_one(self):
        educations=self.driver.find_element_by_id('detailVo_education').find_elements_by_tag_name('option')
        # time.sleep(1)
        for educations in educations:
            if educations.get_attribute('value')=='0':
                educations.click()
                self.assertTrue(educations.is_selected())




    def test_licenseType(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_licenseType_tx=self.driver.find_element_by_id('driverVo_licenseType_tip').text
        self.assertTrue(u'请选择准驾车型.'in driverVo_licenseType_tx)




    def test_licenseType_a(self):
        licenseTypes=self.driver.find_element_by_id('driverVo_licenseType').find_elements_by_tag_name('option')
        for licenseTypes in licenseTypes:
            if licenseTypes.get_attribute('value')=='1':
                licenseTypes.click()
                time.sleep(1)
                self.assertTrue(licenseTypes.is_selected())



    def test_licenseType_b(self):
        licenseTypes=self.driver.find_element_by_id('driverVo_licenseType').find_elements_by_tag_name('option')
        for licenseTypes in licenseTypes:
            if licenseTypes.get_attribute('value')=='2':
                licenseTypes.click()
                time.sleep(1)
                self.assertTrue(licenseTypes.is_selected())


