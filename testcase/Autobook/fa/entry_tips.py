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

    #司机入职付款,预付款为空时提示语
    # #及低于500等提示语    暂时未完成

    def test_entry_tips(self):
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
            self.assertTrue(u'待付款' in flowState_text,'msg')
        time.sleep(2)
        trs1[1].find_element_by_id('entry').click()#点击入职付款
        time.sleep(2)

        #定位入职付款窗口
        entry_table = self.driver.find_element_by_class_name('xubox_main')
        entry_table.find_element_by_id('prepayBalance').click()
        entry_table.find_element_by_id('prepayBalance').clear()
        entry_table.find_element_by_id('entrantSubmit').click()#点击确定入职
        time.sleep(3)

        text = self.driver.switch_to_alert().text
        self.assertEqual(text,u'入职付款失败!预付款不能为空')
        self.driver.switch_to_alert().accept()
        print(text)







