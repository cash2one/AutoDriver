# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'
import time
import unittest
from framework.core import testcase
from drivers import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #司机账户明细交易摘要查询（以工号140017为例）
    def test_drAccount_digest(self):
        time.sleep(2)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('司机账户').click()
        time.sleep(2)

        self.driver.find_element_by_id('driverInfo').clear()
        self.driver.find_element_by_id('driverInfo').send_keys('140017')
        self.driver.find_element_by_id('query').click()#点击查询

        #table1为公司账户列表
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        trs1[1].find_element_by_id('view_driverAccount').click()#进入140017的收支明细列表界面中
        time.sleep(2)

        #1.有结果查询
        self.driver.find_element_by_id('digest').clear()
        self.driver.find_element_by_id('digest').send_keys(u'预付款充值')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出交易摘要，对比信息
        #定位到当前列表
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        for i in range(1,len(trs2)-1):
            tds2 = trs2[i].find_elements_by_tag_name('td')[3]
            digest_text = tds2.get_attribute('title')
            self.assertTrue(u'预付款充值' in digest_text,'msg')
        time.sleep(2)

        #2.模糊查询
        self.driver.find_element_by_id('digest').clear()
        self.driver.find_element_by_id('digest').send_keys(u'退')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出交易摘要，对比信息
        #定位到当前列表
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs3)-1):
            tds3 = trs3[i].find_elements_by_tag_name('td')[3]
            digest_text3 = tds3.get_attribute('title')
            self.assertTrue(u'退' in digest_text3,'msg')
        time.sleep(2)

        #3.无结果查询
        self.driver.find_element_by_id('digest').clear()
        self.driver.find_element_by_id('digest').send_keys(u'ab自动化')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出提示信息，对比信息
        norecords_text = self.driver.find_element_by_class_name('norecords').text
        self.assertTrue(u'没有符合条件的数据...' in norecords_text,'msg')
        time.sleep(2)

if __name__ =='__main__':
    unittest.main()
