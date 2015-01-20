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

    #查询全部
    def test_logall(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #在请求参数文本框里面输入aaaaa
        self.driver.find_element_by_id('platformId').send_keys(u'APP_001')
        self.driver.find_element_by_id('result').send_keys(u'成功')
        self.driver.find_element_by_id('serviceName').send_keys(u'driverService.dealOrde')
        self.driver.find_element_by_id('params').send_keys(u'aaaaa')
        self.driver.find_element_by_id('requestIdSearch').send_keys('14017814213006828048340')
        self.driver.find_element_by_id('content').send_keys(u'{"res":"-2031","msg":"令牌失效"}')
        self.driver.find_element_by_id('query').click()
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
         #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in range(1,len(trs)):
                #找到td
                text1=trs[i].find_elements_by_tag_name('td')[4].text
                text2=trs[i].find_elements_by_tag_name('td')[5].text
                text3=trs[i].find_elements_by_tag_name('td')[6].text
                text4=trs[i].find_elements_by_tag_name('td')[7].text
                text5=trs[i].find_elements_by_tag_name('td')[8].text
                text6=trs[i].find_elements_by_tag_name('td')[9].text
                #判断是不是td里面的  请求参数是不是res":"-2031","msg":"令牌失效
                print text1,i
                print text2,i
                print text3,i
                print text4,i
                print text5,i
                self.assertTrue(u'APP_001' in text1)
                self.assertTrue(u'成功' in text2)
                self.assertTrue(u'driverService.dealOrde' in text3)
                self.assertTrue(u'aaaaa' in text4)
                self.assertTrue(u'14017814213006828048340' in text5)
                self.assertTrue(u'{"res":"-2031","msg":"令牌失效"}' in text6)


