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

    def test_datelist(self):
        '''
        查看合计数目是否正确
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()
        self.driver.find_id('statistics').click()
        time.sleep(5)
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        sum_newCount=0
        for i in range(1,len(trs)):
            newCount=trs[i].find_elements_by_tag_name('td')[1].text
            sum_newCount+=int(newCount)

        table=self.driver.find_element_by_class_name('ui-jqgrid-ftable').find_elements_by_tag_name('tr')[0]
        list_newCount=table.find_elements_by_tag_name('td')[1].text

        self.assertEqual(int(list_newCount),sum_newCount)
