# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_createAccount(self):
        '''
        添加账号，添加成功后，显示在列表第一项
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        n='lishan23'
        r=u'李三56'
        self.driver.find_id('operator_name').send_keys(n)
        self.driver.find_id('operator_realName').send_keys(r)
        ipts=self.driver.find_id('pf2_roles').find_tags('input')
        for ipt in ipts:
            if ipt.get_attribute('title')==u'客服经理':
                ipt.click()
                self.assertTrue(ipt.is_selected())
        self.driver.find_id('operator_mobile').send_keys(u'18155364561')
        self.driver.find_id('operator_email').send_keys(u'18155@qq.com')

        self.driver.find_id('sure_create_account_btn').click()
        self.driver.switch_to_alert()
        text=self.driver.find_class('xubox_dialog').text
        self.assertTrue(u'创建账号成功'in text)
        self.driver.find_element_by_link_text(u'确定').click()

        name=self.driver.find_element_by_id('list').find_tags('tr')[1].find_tags('td')[1].text
        realName=self.driver.find_element_by_id('list').find_tags('tr')[1].find_tags('td')[2].text
        role=self.driver.find_element_by_id('list').find_tags('tr')[1].find_tags('td')[3].text
        self.assertTrue(n in name)
        self.assertTrue(r in realName)
        self.assertTrue(u'客服经理'in role)