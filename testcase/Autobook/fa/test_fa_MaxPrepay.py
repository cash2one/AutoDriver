# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()
    #预付款充值最大金额9999999，对比凭证上的大小写金额是否为9999999
    def test_trade_MaxPrepay(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys('140202')
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('9999999')
        self.driver.find_element_by_id('manul_memo').click()
        self.driver.find_element_by_id('manul_memo').send_keys(u'自动化测试充值最大9999999')
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(4)
        #对比信息:充值司机和充值金额
        driver_text = self.driver.find_element_by_id('pay_confirm_driver').text
        amount_text = self.driver.find_element_by_id('pay_confirm_amount').get_attribute('title')

        print driver_text,amount_text
        self.assertTrue('140202' in driver_text,'msg')
        self.assertTrue(u'9,999,999.00(玖佰玖拾玖万玖仟玖佰玖拾玖元整)' in amount_text,'msg')
        self.driver.find_element_by_id('btn_pay_confirm').click()#点击确定，跳转至打印凭证界面
        time.sleep(3)

        tradeNo_text = self.driver.find_element_by_id('tradeNo').text#取出此次充值记录的交易号
        big_amount = self.driver.find_element_by_id('amountBig').text#取出此次充值凭证上的大写金额
        small_amount = self.driver.find_element_by_id('amount').text#取出此次充值凭证上的小写金额
        print tradeNo_text,small_amount,big_amount#打印交易号，大写金额，小写金额

        self.assertTrue('9,999,999.00' in  small_amount ,'msg')
        self.assertTrue(u'玖佰玖拾玖万玖仟玖佰玖拾玖元整' in  big_amount ,'msg')


        self.driver.find_element_by_id('print_back').click()#返回至充值付款界面
        time.sleep(3)
        #查询此条交易记录的交易号tradeNo_text是否存在于列表中
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')
        for i in range(1,len(trs)):
            tds = trs[i].find_elements_by_tag_name('td')[2]
            if  tds.get_attribute('title') == tradeNo_text:
                print 'Ture',tds.get_attribute('title')
            else:
                print 'False',tds.get_attribute('title')
        time.sleep(3)

