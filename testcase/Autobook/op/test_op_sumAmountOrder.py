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

        self.driver.action_chains().move_to_element(above)
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()
        self.driver.find_id('statistics_amount').click()
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        sum_success=0
        sum_total=0
        sum_fail=0
        for i in range(1,len(trs)):
            success=trs[i].find_elements_by_tag_name('td')[1].text
            fail=trs[i].find_elements_by_tag_name('td')[2].text
            total=trs[i].find_elements_by_tag_name('td')[3].text
            sum_success+=int(success)
            sum_fail+=int(fail)
            sum_total+=int(total)
            print success
        print sum_success,sum_fail,sum_total
        table=self.driver.find_element_by_class_name('ui-jqgrid-ftable').find_elements_by_tag_name('tr')[0]
        list_success=table.find_elements_by_tag_name('td')[1].text
        list_fail=table.find_elements_by_tag_name('td')[2].text
        list_total=table.find_elements_by_tag_name('td')[3].text
        print list_success,list_fail,list_total
        self.assertEqual(sum_success,int(list_success))
        self.assertEqual(sum_fail,int(list_fail))
        self.assertEqual(sum_total,int(list_total))

        success_Rate=float(list_success)/float(list_total)
        text=table.find_elements_by_tag_name('td')[4].text
        list_successRate=filter(str.isdigit, str(text))
        successRate=float( '%.3f' % success_Rate)
        #保留小数点后三位数字
        print successRate,list_successRate
        self.assertTrue(list_successRate in str(successRate))
        #订单成功率=成功订单数/总订单数
