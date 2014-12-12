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
    #押金充值。并查看充值付款界面是否有此记录
    def test_trade_pledgepay(self):

        self.driver.find_element_by_id('trade_pledgepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('driver').click()
        self.driver.find_element_by_id('driver').send_keys('140221')
        self.driver.find_element_by_id('amount').click()
        self.driver.find_element_by_id('amount').send_keys('1')
        self.driver.find_element_by_id('memo').click()
        self.driver.find_element_by_id('memo').send_keys(u'自动化测试充值1元整')
        self.driver.find_element_by_id('btn_pay').click()#点击充值
        time.sleep(4)
        #对比信息:充值司机和充值金额
        driver_text = self.driver.find_element_by_id('pay_confirm_driver').text
        amount_text = self.driver.find_element_by_id('pay_confirm_amount').get_attribute('title')

        print driver_text,amount_text
        self.assertTrue(u'徐小七(140221)' in driver_text,'msg')
        self.assertTrue(u'1.00(壹元整)' in amount_text,'msg')
        self.driver.find_element_by_id('btn_confirm').click()#点击确定，跳转至打印凭证界面
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



if __name__ =='__main__':
    unittest.main()











