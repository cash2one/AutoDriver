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
        # 返回首页
        self.driver.switch_to_home()


    def test_companyAccount_name(self):
        '添加公司账户'
        time.sleep(1)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        self.driver.find_element_by_id('create').click()  #点击添加公司账户
        time.sleep(1)
        self.driver.find_element_by_id('sure_edit_btn').click()  #点击确定
        time.sleep(2)
        tips1_text = self.driver.find_element_by_id('companyAccount_name_edit_tip').text
        print tips1_text
        self.assertTrue(u'账户名称不能为空.' in tips1_text, 'msg')
        time.sleep(2)

        table = self.driver.find_element_by_id('div_edit')  #定位到添加公司账户窗口
        table.find_element_by_id('companyAccount_name_edit').click()
        table.find_element_by_id('companyAccount_name_edit').send_keys('<td><tr>')
        table.find_element_by_id('sure_edit_btn').click()  #点击确定
        tips2_text = table.find_element_by_id('companyAccount_name_edit_tip').text
        print tips2_text
        self.assertTrue(u'账户名称含有非法符号.' in tips2_text, 'msg')


if __name__ == '__main__':
    unittest.main()



