# coding=utf-8
__author__ = 'xiaohengli@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_Appall(self):
        above=self.driver.find_element_by_link_text(u'信息维护')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'APP基本信息').click()
        #在信息标题文本框中输入正常数量的字符
        self.driver.find_element_by_id('title').send_keys('14017814213006828048340')




    def test_Appselect(self):
        above=self.driver.find_element_by_link_text(u'信息维护')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'APP基本信息').click()
         #信息标题不输入任何内容，点击查询
        self.driver.find_element_by_id('query').click()
        #在信息标题中输入标题的部分名称，点击查询
        self.driver.find_element_by_id('title').send_keys(u'车谱')
        self.driver.find_element_by_id('title').send_keys(u'车谱')
        self.driver.find_element_by_id('query').click()

    # def test_Apppage(self):
    #     above=self.driver.find_element_by_link_text(u'信息维护')
    #     self.driver.action_chains().move_to_element(above).perform()
    #      #鼠标悬停在日志查询上
    #     self.driver.find_element_by_link_text(u'APP基本信息').click()
    #     id=self.driver.find_id('first_pager')
    #     #self.assertFalse(id.is_enabled())
    #
    #     #系统自动更新列表记录，底部的当前显示页数也自动更新
    #     self.driver.find_id('next_pager').click()
    #     text=self.driver.find_element_by_class_name('ui-pg-selbox').text
    #     self.assertEqual('2',text)
    #     #"系统自动更新列表记录，底部的当前显示页数也自动更新"
    #     self.driver.find_id('prev_pager').click()
    #     text=self.driver.find_element_by_class_name('ui-pg-selbox').text
    #     self.assertEqual('2',text)
    #     #"首页和上一页按钮呈灰色"
    #     self.driver.find_id('last_pager').click()
    #     #"首页和上一页按钮高亮可操作"
    #     self.driver.find_id('last_pager').click()
    #     #"尾页和下一页按钮呈灰色"
    #     self.driver.find_id('last_pager').click()
    #     #"尾页和下一页按钮高亮可操作"
    #     self.driver.find_id('first_pager').click()
    #     #"系统自动跳转到该页"
    #     time.sleep(1)
    #     self.driver.find_element_by_class_name('ui-pg-input').send_keys("12" + self.driver.keys().RETURN)
    #     text1=self.driver.find_element_by_class_name('ui-pg-selbox').text
    #     self.assertEqual('1',text1)
    #     #"系统默认跳转到第一页"
    #     self.driver.find_element_by_class_name('ui-pg-input').send_keys("1.5" + self.driver.keys().RETURN)
    #     text2=self.driver.find_element_by_class_name('ui-pg-selbox').text
    #     self.assertEqual('1',text2)
    #     #"系统默认跳转到第一页"#在跳转至文本框中输入字母、非法字符，点击回车
    #     self.driver.find_element_by_class_name('ui-pg-input').send_keys("@@@@@" + self.driver.keys().RETURN)
    #     #"系统限制输入"
    #     self.driver.find_element_by_class_name('ui-pg-input').send_keys("1111111111111111111111111111" + self.driver.keys().RETURN)
    #
    #     #"下拉框默认显示20"
    #     trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
    #     opts=self.driver.find_element_by_class_name('ui-pg-selbox').find_elements_by_tag_name('option')
    #
    #     #"下拉框显示选项：10、20、40"
    #     for opt in opts:
    #         #判断text里面的内容等不等于客服专员
    #         if opt.get_attribute('text')=='10':  #获取对象属性
    #             opt.click()
    #             self.assertTrue(len(trs)=='11')
    #             time.sleep(1)
    #
    #         elif opt.get_attribute('text')=='20':
    #             opt.click()
    #             time.sleep(1)
    #             self.assertTrue(len(trs)=='21')
    #
    #         elif opt.get_attribute('text')=='40':
    #             opt.click()
    #             time.sleep(1)
    #             self.assertTrue(len(trs)=='41')
    #
    #
    #
