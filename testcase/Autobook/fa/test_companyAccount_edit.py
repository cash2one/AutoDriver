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

    #公司账户列表操作-修改
    def test_list_operation_edit(self):
        time.sleep(0.5)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')
        trs[1].find_element_by_id('edit').click()#点击第一行修改
        time.sleep(2)

        #修改账户名称、银行账号
        self.driver.find_element_by_id('companyAccount_name_edit').clear()
        self.driver.find_element_by_id('companyAccount_name_edit').send_keys(u'自动化测试账号')

        self.driver.find_element_by_id('companyAccount_bankAccount_edit').clear()
        self.driver.find_element_by_id('companyAccount_bankAccount_edit').send_keys('999999999999999999')

        #点击确定
        self.driver.find_element_by_id('sure_edit_btn').click()
        time.sleep(2)

        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        list_name = trs1[1].find_elements_by_tag_name('td')[1]
        list_bankAccount = trs1[1].find_elements_by_tag_name('td')[4]

        name = list_name.get_attribute('title')#取出账户名称
        bankAccount = list_bankAccount.get_attribute('title')#取出账号

        print name,bankAccount
        self.assertTrue(u'自动化测试账号' in name,'msg')
        self.assertTrue('999999999999999999' in bankAccount,'msg')

        time.sleep(2)

        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        trs3[1].find_element_by_id('edit').click()#点击第一行修改
        time.sleep(2)

        #修改账户名称、银行账号
        self.driver.find_element_by_id('companyAccount_name_edit').clear()
        self.driver.find_element_by_id('companyAccount_name_edit').send_keys(u'预付款账户')

        self.driver.find_element_by_id('companyAccount_bankAccount_edit').clear()
        self.driver.find_element_by_id('companyAccount_bankAccount_edit').send_keys('6545622123123123')

        #点击确定
        self.driver.find_element_by_id('sure_edit_btn').click()
        time.sleep(2)
