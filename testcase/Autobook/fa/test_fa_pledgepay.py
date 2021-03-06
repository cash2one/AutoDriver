# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()
    #押金充值。并查看充值付款界面是否有此记录，查看对应司机账户及公司押金账户是否有记录
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
        self.assertTrue(u'徐小七(140221)' in driver_text,u'充值司机不为140221')
        self.assertTrue(u'1.00(壹元整)' in amount_text,u'充值金额不为1元整')
        self.driver.find_element_by_id('btn_confirm').click()#点击确定，跳转至打印凭证界面
        time.sleep(3)

        tradeNo_text = self.driver.find_element_by_id('tradeNo').text#取出此次充值记录的交易号
        print tradeNo_text
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

        #成功充值后，查询对应司机账户明细是否有记录
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('司机账户').click()
        time.sleep(2)
        self.driver.find_element_by_id('driverInfo').click()#输入查询条件140017
        self.driver.find_element_by_id('driverInfo').send_keys('140221')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        self.driver.find_element_by_id('view_driverAccount').click()#点击明细
        time.sleep(2)
        #查询此条交易记录的交易号tradeNo_text是否存在于司机明细列表中
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        for i in range(1,len(trs1)):
            tds1 = trs1[i].find_elements_by_tag_name('td')[1]
            if  tds1.get_attribute('title') == tradeNo_text:
                print 'Ture',tds1.get_attribute('title')
            else:
                print 'False',tds1.get_attribute('title')
        time.sleep(2)

        #成功充值后，查询公司预付款账户明细是否有记录
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        trs2[16].find_element_by_id('detail').click()
        time.sleep(2)

        #查询此条交易记录的交易号tradeNo_text是否存在于公司预付款账户明细列表中
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs1)):
            tds3 = trs3[i].find_elements_by_tag_name('td')[1]
            if  tds3.get_attribute('title') == tradeNo_text:
                print 'Ture',tds3.get_attribute('title')
            else:
                print 'False',tds3.get_attribute('title')
        time.sleep(2)
