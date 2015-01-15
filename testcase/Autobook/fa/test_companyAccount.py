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
    #添加公司账户
    def test_companyAccount(self):
        time.sleep(1)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        self.driver.find_element_by_id('create').click()#点击添加公司账户
        time.sleep(1)
        # 点击取消
        self.driver.find_element_by_id('cancle_btn').click()
        time.sleep(1)

        self.driver.find_element_by_id('create').click()#点击添加公司账户
        time.sleep(1)
        table1 = self.driver.find_element_by_id('xubox_layer2')#定位到当前div
        # 点击X号关闭窗口
        table1.find_element_by_class_name('xubox_close').click()
        time.sleep(1)

        self.driver.find_element_by_id('create').click()#点击添加公司账户
        time.sleep(1)

        table = self.driver.find_element_by_id('div_edit')#定位到添加公司账户窗口
        #添加账户名称
        table.find_element_by_id('companyAccount_name_edit').click()
        table.find_element_by_id('companyAccount_name_edit').send_keys(u'自动化测试账户')
        #选择账户类型-收入账户
        table.find_element_by_id('companyAccount_type_edit').find_elements_by_tag_name('option')[3].click()
        #选择所属银行-中国光大银行-索引13
        table.find_element_by_id('companyAccount_bank_edit').find_elements_by_tag_name('option')[13].click()
        #添加银行账号
        table.find_element_by_id('companyAccount_bankAccount_edit').click()
        table.find_element_by_id('companyAccount_bankAccount_edit').send_keys('12345678902145233')

        #添加户主信息
        table.find_element_by_id('companyAccount_bankHolder_edit').click()
        table.find_element_by_id('companyAccount_bankHolder_edit').send_keys('12345678902145233')
        #添加开户行信息
        table.find_element_by_id('companyAccount_bankAddr_edit').click()
        table.find_element_by_id('companyAccount_bankAddr_edit').send_keys('12345678902145233')
        #添加备注信息
        table.find_element_by_id('companyAccount_memo_edit').click()
        table.find_element_by_id('companyAccount_memo_edit').send_keys('12345678902145233')

        #table.find_element_by_id('sure_edit_btn').click()#点击确定


if __name__ == '__main__':
    unittest.main()




