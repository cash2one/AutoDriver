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

    #司机入职付款,应付金额数值变化，等于应付押金加上填入的应付服务费+应付押金
    #entry_pledge = '50000'
    def test_entry_totalAmount(self):
        '#司机入职付款,应付金额数值变化，等于应付押金加上填入的应付服务费+应付押金'
        time.sleep(1)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('司机账户').click()
        time.sleep(2)

        #查询一入职付款司机
        self.driver.find_element_by_id('driverInfo').clear()
        self.driver.find_element_by_id('driverInfo').send_keys('150002')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(1)

        #table1为当前司机账户列表
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')

        for i in range(1,len(trs1)):
            tds1 = trs1[i].find_elements_by_tag_name('td')[3]
            flowState_text = tds1.get_attribute('title')
            self.assertTrue(u'待付款' in flowState_text,u'没有找到指定字符串')
        time.sleep(2)
        trs1[1].find_element_by_id('entry').click()#点击入职付款
        time.sleep(2)

        #定位入职付款窗口
        entry_table = self.driver.find_element_by_class_name('xubox_main')
        entry_table.find_element_by_id('prepayBalance').click()
        entry_table.find_element_by_id('prepayBalance').clear()
        entry_table.find_element_by_id('prepayBalance').send_keys('50000')
        pledgeBalance = entry_table.find_element_by_id('pledgeBalance').text
        totalAmount = entry_table.find_element_by_id('totalAmount').text
        pledgeBalance_int = self.driver.to_int(pledgeBalance)
        totalAmount_int = self.driver.to_int(totalAmount)

        print pledgeBalance,totalAmount
        print pledgeBalance_int,totalAmount_int
        self.assertTrue(totalAmount_int == pledgeBalance_int + 50000,u'应付金额不等于输入的应付服务费与应付押金之和')

        time.sleep(3)








