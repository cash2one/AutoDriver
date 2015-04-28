# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from drivers import *
import datetime


time1='2015-01-06'#开始时间
time2='2015-01-15'#结束时间

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_datelist(self):
        '''
        不选择开始时间及结束时间，提交后，列表中默认显示本月1号到前一天的订单记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above)
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        startTime_id=self.driver.find_id('startTime_amount')
        startTime_text=startTime_id.get_attribute("value")
        endTime_id=self.driver.find_id('endTime_amount')
        endTime_text=endTime_id.get_attribute("value")
        #获取时间控件中的开始日期及结束日期
        year=datetime.date.today().year
        month=datetime.date.today().month
        startTime1=datetime.date(year,month,01)
        endTime1=datetime.date.today()-datetime.timedelta(days=1)
        self.driver.find_id('statistics_amount').click()
        #选择结束时间
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_tags('tr')
        start=trs[1].find_tags('td')[0].text
        startTime=start[0:4]+'-'+start[5:7]+'-'+start[-3:-1]
        end=trs[len(trs)-1].find_tags('td')[0].text
        endTime=end[0:4]+'-'+end[5:7]+'-'+end[-3:-1]
        print startTime1,endTime1
        print startTime_text,endTime_text
        self.assertEqual(startTime_text,str(startTime1),u'时间控件的默认开始时间不是本月第一天')
        self.assertEqual(str(startTime1),startTime,u'列表第一项不是显示的本月第一天')
        self.assertEqual(endTime_text,str(endTime1),u'时间控件的默认结束时间不是前一天')
        self.assertEqual(str(endTime1),endTime,u'列表最后一项显示的不是前一天的')

    def test_datelist1(self):
        '''
        选择开始时间及结束时间，提交后，列表中显示该时间范围内的订单记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        js = '$(\'input[id=startTime_amount]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime_amount').clear()

        self.driver.find_element_by_id('startTime_amount').send_keys(time1)
        #选择开始时间
        js = '$(\'input[id=endTime_amount]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime_amount').clear()

        self.driver.find_element_by_id('endTime_amount').send_keys(time2)
        self.driver.find_id('statistics_amount').click()
        #选择结束时间
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_tags('tr')
        start=trs[1].find_tags('td')[0].text
        startTime=start[0:4]+'-'+start[5:7]+'-'+start[-3:-1]
        end=trs[len(trs)-1].find_tags('td')[0].text
        endTime=end[0:4]+'-'+end[5:7]+'-'+end[-3:-1]
        self.assertEqual(time1,startTime,u'列表第一项显示的不是所选的开始时间')
        self.assertEqual(time2,endTime,u'列表第一项显示的不是所选的结束时间')

