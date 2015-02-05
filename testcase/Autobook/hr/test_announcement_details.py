# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()
        # 关闭浏览器
        # self.driver.close()

    #发布公告
    def test_announcement(self):
       '''
        对比显示信息是否一致，不一致显示"与对比值不一致"
        :return:
        '''
       self.driver.find_element_by_link_text(u'司机管理').click()
       self.driver.find_element_by_link_text(u'发布公告').click()
       self.driver.find_element_by_id('title').send_keys(u'汽车代驾服务')
       self.driver.find_element_by_id('content').send_keys(u'指汽车代驾公司为单位或个人临时或长期提供经验丰富的汽车代驾司机驾驶车辆的一种汽车代驾服务。')
       tittx=self.driver.find_element_by_id('title').get_attribute('value')
       self.assertTrue(u'汽车代驾服务' in tittx,u'输入内容错误')
       contx=self.driver.find_element_by_id('content').get_attribute('value')
       self.assertTrue(u'指汽车代驾公司为单位或个人临时或长期提供经验丰富的汽车代驾司机驾驶车辆的一种汽车代驾服务。' in contx,u'输入内容错误')
       # 点击确定按钮
       self.driver.find_element_by_id('noticeSubmit').click()
       self.assertTrue(u'发布公告' in self.driver.title,u'界面跳转错误')
       #点击公告管理
       self.driver.find_element_by_link_text(u'公告管理').click()
       tds=self.driver.find_id('list').find_tags('tr')[1].find_tags('td')
       # titletx=tds[1].text
       contenttx=tds[6].text
       ccontx=contenttx[4]
       print ccontx
       # contenttx.find_element_by_link_text(u'公告详情').click()
       # print self.driver.find_id('title').text
       # print self.driver.find_id('number').text
       # print self.driver.find_id('noticeTime').text
       # print self.driver.find_id('content').text
       # self.assertEqual(u'汽车代驾服务',titletx,u'第一行详情标题')
       # self.assertEqual(u'指汽车代驾公司为单位或个人临时或长期提供经验丰富的汽车代驾司机驾驶车辆的一种汽车代驾服务。',contenttx,u'第一行详情内容')


