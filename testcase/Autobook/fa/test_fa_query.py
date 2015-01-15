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

    #①交易号查询：查询此交易号141802170113098250记录，
    def test_tranNo_query(self):

        self.driver.find_element_by_id('tranNo').click()
        self.driver.find_element_by_id('tranNo').send_keys('141802170113098250')
        self.driver.find_element_by_id('query').click()
        time.sleep(2)
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        tds1 = trs1[1].find_elements_by_tag_name('td')[2]
        if  tds1.get_attribute('title') == '141802170113098250':
            print 'Ture',tds1.get_attribute('title')
        else:
            print 'False'
        time.sleep(1)

    #②交易类型查询：查询预付款充值类型记录
    def test_List_type_query(self):

        self.driver.find_element_by_id('tranNo').clear()
        self.driver.find_element_by_id('type').find_elements_by_tag_name('option')[1].click()
        self.driver.find_element_by_id('query').click()
        time.sleep(3)
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        for i in range(1,len(trs2)-1):
            tds2 = trs2[i].find_elements_by_tag_name('td')[3]
            if  tds2.get_attribute('title') == u'预付款充值':
                print 'Ture'
            else:
                print 'False'
        time.sleep(3)

    #③付款方式查询：查询付款方式-页面导入，记录
    def test_tradeOperateType_query(self):

        self.driver.find_element_by_id('tradeOperateType').find_elements_by_tag_name('option')[2].click()
        self.driver.find_element_by_id('query').click()
        time.sleep(2)
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs3)-1):
            tds3 = trs3[i].find_elements_by_tag_name('td')[6]
            if  tds3.get_attribute('title') == u'页面导入':
                print 'Ture'
            else:
                 print 'False'
        time.sleep(1)

    #④司机名称或司机工号查询：查询司机工号140017
    def test_driverInfo_query(self):

        self.driver.find_element_by_id('tranNo').clear()
        self.driver.find_element_by_id('driverInfo').click()
        self.driver.find_element_by_id('driverInfo').send_keys('140017')
        self.driver.find_element_by_id('query').click()
        time.sleep(3)
        table4 = self.driver.find_element_by_id('list')
        trs4 = table4.find_elements_by_tag_name('tr')
        for i in range(0,len(trs4)-1):
            tds4 = trs4[i].find_elements_by_tag_name('td')[4]
            if  tds4.get_attribute('title') == u'司马小二啊哈(140017)':
                print 'Ture'
            else:
                 print 'False'
        time.sleep(3)

if __name__ =='__main__':
    unittest.main()

