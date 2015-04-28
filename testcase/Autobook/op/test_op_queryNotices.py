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

    def test_queryNotice1(self):
        '''
        查询条件中输入'通知'，列表中显示标题及内容包含'通知'的公告
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()
        self.driver.find_id('noticeInfo').send_keys(u'通知')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')
        list_title=[]
        list_content=[]
        if len(trs)>1:
            for i in range(1,len(trs)):
                title=trs[i].find_tags('td')[1].text
                content=trs[i].find_tags('td')[2].text
                if u'通知'in title:
                    list_title.append(title)
                elif u'通知'in content:
                    list_content.append(content)
                time.sleep(3)
            self.assertTrue(len(list_title)>1 or len(list_content)>1)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)
