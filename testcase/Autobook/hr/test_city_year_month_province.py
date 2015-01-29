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

    def test_city(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_city_tx=self.driver.find_element_by_id('driverVo_city_tip').text
        self.assertTrue(u'请选择城市.'in driverVo_city_tx)

    def test_city1(self):

        citys=self.driver.find_element_by_id('driverVo_city').find_elements_by_tag_name('option')
        # time.sleep(1)
        for city in citys:
            if city.get_attribute('value')=='-99':
                city.click()
                self.assertTrue(city.is_selected())

    def test_city2(self):

        citys=self.driver.find_element_by_id('driverVo_city').find_elements_by_tag_name('option')
        # time.sleep(1)
        for city in citys:
            if city.get_attribute('value')=='1':
                city.click()
                self.assertTrue(city.is_selected())
#

    def test_year(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_year_tx=self.driver.find_element_by_id('year_tip').text
        self.assertTrue(u'请选择年份.'in driverVo_year_tx)

    def test_year1(self):
        years=self.driver.find_element_by_id('year').find_elements_by_tag_name('option')
        # time.sleep(1)
        for year in years:
            if year.get_attribute('value')=='-99':
                year.click()
                self.assertTrue(year.is_selected())

    def test_year2(self):
        years=self.driver.find_element_by_id('year').find_elements_by_tag_name('option')
        # time.sleep(1)
        for year in years:
            if year.get_attribute('value')=='1995':
               year.click()
               self.assertTrue(year.is_selected())

    def test_month(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_month_tx=self.driver.find_element_by_id('month_tip').text
        self.assertTrue(u'请选择月份.'in driverVo_month_tx)

    def test_month1(self):
        months=self.driver.find_element_by_id('month').find_elements_by_tag_name('option')
        # time.sleep(1)
        for month in months:
            if month.get_attribute('value')=='-99':
                month.click()
                self.assertTrue(month.is_selected())

    def test_month2(self):
        months=self.driver.find_element_by_id('month').find_elements_by_tag_name('option')
        # time.sleep(1)
        for month in months:
            if month.get_attribute('value')=='1':
                month.click()
                self.assertTrue(month.is_selected())


    def test_province(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_province_tx=self.driver.find_element_by_id('driverVo_province_tip').text
        self.assertTrue(u'请选择籍贯.'in driverVo_province_tx)

    def test_province1(self):
        provinces=self.driver.find_element_by_id('driverVo_province').find_elements_by_tag_name('option')
        # time.sleep(1)
        for province in provinces:
            if province.get_attribute('value')=='-99':
                province.click()
                self.assertTrue(province.is_selected())

    def test_province2(self):
        provinces=self.driver.find_element_by_id('driverVo_province').find_elements_by_tag_name('option')
        # time.sleep(1)
        for province in provinces:
            if province.get_attribute('value')=='1':
                province.click()
                self.assertTrue(province.is_selected())





