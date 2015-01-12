# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'

import time
import unittest
from framework.core import idriver_web

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()
    #预付款充值,充值司机不存在
    #充值司机输入司机的姓（如:张）
    def test_NoDriver_tips1(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys(u'张')#充值司机输入司机的姓（如:张）
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(2)
        #对比界面红色字体提示语
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        print driver_tip_text
        self.assertTrue(u'充值司机不存在.' in driver_tip_text,'msg')
        time.sleep(1)

    #充值司机输入司机的全名（如：周大福）
    def test_NoDriver_tips2(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys(u'周大福')#充值司机输入司机的全名（如：周大福）
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(2)
        #对比界面红色字体提示语
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        print driver_tip_text
        self.assertTrue(u'充值司机不存在.' in driver_tip_text,'msg')
        time.sleep(1)

    #充值司机输入字母（如：abc）
    def test_NoDriver_tips3(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys('abc')#充值司机输入字母（如：abc）
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(2)
        #对比界面红色字体提示语
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        print driver_tip_text
        self.assertTrue(u'充值司机不存在.' in driver_tip_text,'msg')
        time.sleep(1)

    #充值司机输入html标签（如：<tr>）
    def test_NoDriver_tips4(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys('<tr>')#充值司机输入html标签（如：<tr>）
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(2)
        #对比界面红色字体提示语
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        print driver_tip_text
        self.assertTrue(u'充值司机不存在.' in driver_tip_text,'msg')
        time.sleep(1)

    #充值司机输入特殊字符
    def test_NoDriver_tips5(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys(u'！@#@%￥……&')#充值司机输入特殊字符
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(2)
        #对比界面红色字体提示语
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        print driver_tip_text
        self.assertTrue(u'充值司机不存在.' in driver_tip_text,'msg')
        time.sleep(1)

    #充值司机输入不存在的工号（如：14001）
    def test_NoDriver_tips6(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys('14001')#充值司机输入不存在的工号（如：14001）
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(2)
        #对比界面红色字体提示语
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        print driver_tip_text
        self.assertTrue(u'充值司机不存在.' in driver_tip_text,'msg')
        time.sleep(1)

    #充值司机输入已经离职的司机工号（如：140083）
    def test_NoDriver_tips7(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys('140083')#充值司机输入已经离职的司机工号（如：140083）
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(2)
        #对比界面红色字体提示语
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        print driver_tip_text
        self.assertTrue(u'充值司机不存在.' in driver_tip_text,'msg')
        time.sleep(1)


if __name__ =='__main__':
    unittest.main()


