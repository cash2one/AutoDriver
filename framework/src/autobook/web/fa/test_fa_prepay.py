__author__ = 'xuguanghua@pathbook.com.cn'
# coding=utf-8
#查询成功

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
    #预付款充值,手动方式充值
    def test_trade_prepay(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys('140017')
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('manul_memo').click()
        self.driver.find_element_by_id('manul_memo').send_keys(u'自动化测试充值1元整')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(4)
        #对比信息:充值司机和充值金额
        driver_text = self.driver.find_element_by_id('pay_confirm_driver').text
        amount_text = self.driver.find_element_by_id('pay_confirm_amount').get_attribute('title')

        print driver_text,amount_text
        self.assertTrue(u'司马小二啊哈(140017)' in driver_text,'msg')
        self.assertTrue(u'1.00(壹元整)' in amount_text,'msg')
        self.driver.find_element_by_id('btn_pay_confirm').click()#点击确定，跳转至打印凭证界面
        time.sleep(3)

        tradeNo_text = self.driver.find_element_by_id('tradeNo').text#取出此次充值记录的交易号
        print tradeNo_text
        self.driver.find_element_by_id('print_back').click()#返回至充值付款界面
        time.sleep(3)
        #查询此条交易记录的交易号tradeNo_text是否存在于列表中
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')
        for i in range(0,len(trs)-1):
            tds = trs[i].find_elements_by_tag_name('td')
            if  tds[1].text == tradeNo_text:
                break
        time.sleep(3)













