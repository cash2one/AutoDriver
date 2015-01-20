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
    #添加公司账户,账户类型，所属银行、银行账户未填入信息
    def test_companyAccount(self):
        time.sleep(1)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        self.driver.find_element_by_id('create').click()#点击添加公司账户
        time.sleep(1)
        table=self.driver.find_element_by_id('div_edit')#定位到添加公司账户窗口
        table.find_element_by_id('sure_edit_btn').click()#点击确定
        time.sleep(2)
        tips1_text = table.find_element_by_id('companyAccount_type_edit_tip').text
        tips2_text = table.find_element_by_id('companyAccount_bank_edit_tip').text
        tips3_text = table.find_element_by_id('companyAccount_bankAccount_edit_tip').text
        print tips1_text,tips2_text,tips3_text
        self.assertTrue(u'请选择账户类型.' in tips1_text,'msg')
        self.assertTrue(u'请选择所属银行.' in tips2_text,'msg')
        self.assertTrue(u'银行账号不能为空.' in tips3_text,'msg')
        opts1 = table.find_element_by_id('companyAccount_type_edit').find_elements_by_tag_name('option')
        opts2 = table.find_element_by_id('companyAccount_bank_edit').find_elements_by_tag_name('option')
        print len(opts1)-1,len(opts2)-1
        time.sleep(2)

    #添加公司账户,银行账户输入信息
    def test_companyAccount_bankAccount(self):
        time.sleep(1)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        self.driver.find_element_by_id('create').click()#点击添加公司账户
        time.sleep(1)
        table=self.driver.find_element_by_id('div_edit')#定位到添加公司账户窗口
        table.find_element_by_id('companyAccount_bankAccount_edit').click()
        table.find_element_by_id('companyAccount_bankAccount_edit').send_keys('<tr><td>')
        table.find_element_by_id('sure_edit_btn').click()#点击确定
        time.sleep(2)
        tips4_text = table.find_element_by_id('companyAccount_bankAccount_edit_tip').text
        print tips4_text
        self.assertTrue(u'银行账号必须为15到20位的数字.' in tips4_text,'msg')
        time.sleep(2)
        #账号输入14位数字
        table.find_element_by_id('companyAccount_bankAccount_edit').clear()
        table.find_element_by_id('companyAccount_bankAccount_edit').send_keys('12345678901234')
        table.find_element_by_id('sure_edit_btn').click()#点击确定
        time.sleep(2)
        tips5_text = table.find_element_by_id('companyAccount_bankAccount_edit_tip').text
        print tips5_text
        self.assertTrue(u'银行账号必须为15到20位的数字.' in tips5_text,'msg')
        time.sleep(2)
        #账号输入21位数字
        table.find_element_by_id('companyAccount_bankAccount_edit').clear()
        table.find_element_by_id('companyAccount_bankAccount_edit').send_keys('123456789012345612304')
        table.find_element_by_id('sure_edit_btn').click()#点击确定
        time.sleep(2)
        tips6_text = table.find_element_by_id('companyAccount_bankAccount_edit_tip').text
        print tips6_text
        self.assertTrue(u'银行账号必须为15到20位的数字.' in tips6_text,'msg')
        time.sleep(2)
        #账号输入包含英文、小数点
        table.find_element_by_id('companyAccount_bankAccount_edit').clear()
        table.find_element_by_id('companyAccount_bankAccount_edit').send_keys('12345678901ACVbd...22')
        table.find_element_by_id('sure_edit_btn').click()#点击确定
        time.sleep(2)
        tips7_text = table.find_element_by_id('companyAccount_bankAccount_edit_tip').text
        print tips7_text
        self.assertTrue(u'银行账号必须为15到20位的数字.' in tips7_text,'msg')
        time.sleep(2)
