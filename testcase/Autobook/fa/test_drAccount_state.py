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

    #司机账户账户状态查询，全部状态、正常、冻结
    def test_drAccount_state(self):
        time.sleep(2)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('司机账户').click()
        time.sleep(2)
        #取出默认的账户状态，正常为真
        state_default = self.driver.find_element_by_id('state').text
        self.assertTrue(u'正常' in state_default,u'没有找到指定字符串')
        #取出当前列表账户状态文本，正常为真
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        for i in range(1,len(trs1)):
            tds1 = trs1[i].find_elements_by_tag_name('td')[9]
            state1_text = tds1.get_attribute('title')
            self.assertTrue(u'正常' in state1_text,u'没有找到指定字符串')
        time.sleep(2)
        #取出账户正常状态的司机记录数
        pager = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        #正常状态下的司机记录数为
        list_normalNo = (int(pager)-1)*20+len(trs2)-1
        print '账户状态为正常的记录数为：',list_normalNo,'条'
        time.sleep(2)

        #点击已冻结
        self.driver.find_element_by_id('state').find_elements_by_tag_name('option')[2].click()
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出当前列表账户状态文本，已冻结为真
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs3)):
            tds3 = trs3[i].find_elements_by_tag_name('td')[9]
            state2_text = tds3.get_attribute('title')
            self.assertTrue(u'已冻结' in state2_text,u'没有找到指定字符串')
        time.sleep(2)
        #取出账户已冻结状态的司机记录数
        pager1 = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table4 = self.driver.find_element_by_id('list')
        trs4 = table4.find_elements_by_tag_name('tr')
        #账户状态为已冻结的记录数为
        list_freezeNo = (int(pager1)-1)*20+len(trs4)-1
        print '账户状态为已冻结的记录数为：',list_freezeNo,'条'
        time.sleep(2)

        #点击全部账户状态
        self.driver.find_element_by_id('state').find_elements_by_tag_name('option')[0].click()
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出全部账户状态的记录数
        pager2 = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table5 = self.driver.find_element_by_id('list')
        trs5 = table5.find_elements_by_tag_name('tr')
        #全部账户状态的记录数为
        list_No = (int(pager2)-1)*20+len(trs5)-1
        print '全部账户状态的记录数',list_No,'条'
        time.sleep(2)
        #对比：若账户全部状态的记录数=正常记录数+已冻结记录数，为真
        self.assertTrue(list_No == list_normalNo + list_freezeNo,u'若账户全部状态的记录数不等于正常记录数加已冻结记录数')
