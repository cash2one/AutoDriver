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
    #充值付款界面，点击详情并对比信息
    def test_view_trade(self):
        time.sleep(1)

        #取出列表第二行的充值记录信息，索引[3]
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')
        list_no = trs[2].find_elements_by_tag_name('td')[2]
        list_no_text = list_no.get_attribute('title')#取出交易号
        list_type = trs[2].find_elements_by_tag_name('td')[3]
        list_type_text = list_type.get_attribute('title')#取出交易类型
        list_operateType = trs[2].find_elements_by_tag_name('td')[6]
        list_operateType_text = list_operateType.get_attribute('title')#取出付款方式

        print list_no_text,list_type_text,list_operateType_text

        trs[2].find_element_by_id('view_trade').click()#点击列表第二行的详情，打开查看交易信息窗口
        time.sleep(2)

        table2 = self.driver.find_element_by_id('trade_base_info')#定位到查看交易信息窗口

        tranNo = table2.find_element_by_id('tranNo').text#取出查看交易信息窗口的交易号
        tradeType = table2.find_element_by_id('tradeType').text#取出查看交易信息窗口的交易类型
        operateType = table2.find_element_by_id('operateType').text#取出查看交易信息窗口的付款方式

        print tranNo,tradeType,operateType
        #对比信息
        if (list_no_text == tranNo)&(list_type_text == tradeType)&(list_operateType_text == operateType):
            print 'Ture'
        else:
            print 'False'


if __name__ =='__main__':
    unittest.main()
