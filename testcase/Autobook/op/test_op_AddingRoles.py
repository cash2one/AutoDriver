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

    def test_selectAllLimit(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('create').click()
        #进入角色添加页面
        self.driver.find_id('role_name').send_keys(u'运维超级管理员2')
        opts=self.driver.find_id('role_platformType').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'运维':  #获取对象属性
                opt.click()
        self.driver.find_element_by_id('allLimit').click()
        self.driver.find_id('role_memo').send_keys(u'此角色拥有全部财务权限')
        self.driver.find_id('sure_create_role_btn').click()
        self.driver.switch_to_alert()
        time.sleep(2)
        text=self.driver.find_element_by_class_name('xubox_main').text
        self.assertTrue(u"添加角色成功" in text)
        self.driver.find_element_by_xpath(u'/html/body/div[5]/div[1]/span[2]/a').click()
        type=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text
        name=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[2].text
        memo=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[3].text
        self.assertTrue(type==u'运维')
        self.assertTrue(name==u'运维超级管理员2')
        self.assertTrue(memo==u'此角色拥有全部财务权限')

