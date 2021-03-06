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

    def test_viewRole(self):
        '''
        修改角色
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('editRole').click()
        #进入角色查看页面
        self.assertEqual(self.driver.title,u'编辑角色')
        self.driver.find_id('role_name').clear()
        self.driver.find_id('role_name').send_keys(u'客服管理员zw')
        self.driver.find_id('limits').click()
        self.driver.find_id('role_memo').clear()
        self.driver.find_id('role_memo').send_keys(u'此管理员拥有与之前相反的权限')
        self.driver.find_id('sure_edit_role_btn').click()
        text=self.driver.find_class('xubox_dialog').text
        print text
        self.assertTrue(u"编辑角色成功!"in text)
        self.driver.find_class('xubox_botton').click()
        time.sleep(3)
        type=self.driver.find_id('list').find_tags('tr')[1].find_tags('td')[1].text
        name=self.driver.find_id('list').find_tags('tr')[1].find_tags('td')[2].text
        memo=self.driver.find_id('list').find_tags('tr')[1].find_tags('td')[3].text
        self.assertTrue(type==u'客服')
        self.assertTrue(name==u'客服管理员zw')
        self.assertTrue(memo==u'此管理员拥有与之前相反的权限')
