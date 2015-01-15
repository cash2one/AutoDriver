# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'



import time
import unittest
from framework.core import testcase
from selenium.common import exceptions

class TestCase(unittest.TestCase):
    '''
    单个条件查询成功
    '''

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #根据订单号查询
    def test_order_query(self):

        time.sleep(2)
        table=self.driver.find_element_by_id('list')
        trs=table.find_elements_by_tag_name('tr')
        #取第一行第一列的订单号
        tds=trs[1].find_elements_by_tag_name('td')
        order=tds[1].text
        self.driver.find_element_by_id('orderNo').send_keys(order)
        time.sleep(1)
        #选择“全部任务”查询条件
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'全部任务':
                opt.click()
        self.driver.find_element_by_id('query').click()
        time.sleep(2)
        #获取查询结果中的订单号
        trs1=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        #取第一行第一列的订单号
        tds1=trs1[1].find_elements_by_tag_name('td')
        order1=tds1[1].text
        #对比两个订单是否相等
        self.assertTrue(order in order1,'msg')



    def test_customerName_query(self):

        self.driver.find_ajax_id('customerInfo')
        self.driver.find_element_by_id('customerInfo').send_keys('wss')
        time.sleep(1)
        #选择“全部任务”查询条件
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'全部任务':
                opt.click()
        self.driver.find_element_by_id('query').click()
        time.sleep(4)
        #获取查询结果中的name
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        #取第一行第一列的订单号
        for i in range(1,len(trs)-1):
         tds=trs[i].find_elements_by_tag_name('td')[3]
         # order1=tds[i].text
         print tds.text
         # time.sleep(1)
         self.assertTrue(u'wss' in tds.text,'msg')


    def test_customerPhone_query(self):

        self.driver.find_ajax_id('customerInfo')
        self.driver.find_element_by_id('customerInfo').send_keys('13636468713')
        time.sleep(1)
        #选择“全部任务”查询条件
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'全部任务':
                opt.click()
        self.driver.find_element_by_id('query').click()
        time.sleep(4)
        #获取查询结果中的name(phone)
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        #取所有行第3列
        for i in range(1,len(trs)-1):
         tds=trs[i].find_elements_by_tag_name('td')[3]
         # order1=tds[i].text
         print tds.text
         # time.sleep(1)
         self.assertTrue(u'13636468713' in tds.text,'msg')


    def test_driverName_query(self):

        self.driver.find_ajax_id('driverInfo')
        self.driver.find_element_by_id('driverInfo').send_keys('康小伟')
        time.sleep(1)
        #选择“全部任务”查询条件
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'全部任务':
                opt.click()
        self.driver.find_element_by_id('query').click()
        time.sleep(4)
        #获取查询结果中所有行的第三列
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        for i in range(1,len(trs)-1):
         tds=trs[i].find_elements_by_tag_name('td')[4]
         # order1=tds[i].text
         print tds.text
         # time.sleep(1)
         self.assertTrue(u'康小伟' in tds.text,'msg')

    def test_driverPhone_query(self):

        self.driver.find_ajax_id('driverInfo')
        self.driver.find_element_by_id('driverInfo').send_keys('140018')
        time.sleep(1)
        #选择“全部任务”查询条件
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'全部任务':
                opt.click()
        self.driver.find_element_by_id('query').click()
        time.sleep(4)
        #获取查询结果中所有行的第三列
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        for i in range(1,len(trs)-1):
         tds=trs[i].find_elements_by_tag_name('td')[4]
         # order1=tds[i].text
         print tds.text
         # time.sleep(1)
         self.assertTrue(u'140018' in tds.text,'msg')





