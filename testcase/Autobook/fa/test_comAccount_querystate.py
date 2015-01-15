# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'
import time
import unittest
from framework.core import testcase

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #公司账户明细收支状态查询（默认的预付款账户为例）
    def test_comAccount_balanceState(self):
        time.sleep(0.5)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        #table1为公司账户列表
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        trs1[17].find_element_by_id('detail').click()#进入此账户收支明细列表界面中
        time.sleep(2)

        self.driver.find_element_by_id('balanceState').find_elements_by_tag_name('option')[1].click()#点击收支框收入项
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出支出列，支出为0.00为真
        #定位当前列表
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        for i in range(1,len(trs2)-1):
            tds2 = trs2[i].find_elements_by_tag_name('td')[5]
            balanceOut_text = tds2.get_attribute('title')
            print balanceOut_text
            self.assertTrue(balanceOut_text == '0.00','msg')

        time.sleep(2)

        self.driver.find_element_by_id('balanceState').find_elements_by_tag_name('option')[2].click()#点击收支框支出项
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出收入列，收入为0.00为真
        #定位当前列表
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs3)-1):
            tds3 = trs3[i].find_elements_by_tag_name('td')[4]
            balanceIn_text = tds3.get_attribute('title')
            print balanceIn_text
            self.assertTrue(balanceIn_text == '0.00','msg')
        time.sleep(2)


