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
       gltx=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').text
       print gltx
       self.assertTrue(u'司机管理' in gltx,u'与对比值不一致')
       self.driver.find_element_by_link_text(u'司机管理').click()
       addtx=self.driver.find_element_by_id('release').text
       self.assertTrue(u'发布公告' in addtx,u'与对比值不一致')
       self.driver.find_element_by_link_text(u'发布公告').click()
       tit=self.driver.find_element_by_xpath('/html/body/div[3]/div[1]').text
       print tit
       self.assertTrue(u'发布公告' in addtx,u'与对比值不一致')

    def test_announcement_driver(self):
       self.driver.find_element_by_link_text(u'司机管理').click()
       self.driver.find_element_by_link_text(u'发布公告').click()
       # 司机总人数
       nutx=self.driver.find_element_by_id('number').text
       print nutx
       # 查看司机
       self.driver.find_element_by_link_text(u'查看司机').click()
       self.driver.switch_to_alert()
       self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/span[1]/a').click()

    # 公告内容都为空
    def test_announcement_null(self):
       '''
       公告内容错误，对比提示是否一致，不一致显示"提示信息错误"
       :return:
       '''
       self.driver.find_element_by_link_text(u'司机管理').click()
       self.driver.find_element_by_link_text(u'发布公告').click()
       self.driver.find_element_by_id('noticeSubmit').click()
       tittx=self.driver.find_element_by_id('title_tip').text
       self.assertTrue(u'标题不能为空.' in tittx,u'提示信息错误')
       contx=self.driver.find_element_by_id('content_tip').text
       self.assertTrue(u'内容不能为空.' in contx,u'提示信息错误')

    def test_announcement_null1(self):
       '''
       公告内容错误，对比提示是否一致，不一致显示"提示信息错误"
       :return:
       '''
       self.driver.find_element_by_link_text(u'司机管理').click()
       self.driver.find_element_by_link_text(u'发布公告').click()
       self.driver.find_element_by_id('title').send_keys(u'')
       self.driver.find_element_by_id('content').send_keys(u'代驾租车是由出租方提供车辆及驾驶人员的汽车租赁方式。')
       self.driver.find_element_by_id('noticeSubmit').click()
       tittx=self.driver.find_element_by_id('title_tip').text
       self.assertTrue(u'标题不能为空.' in tittx,u'提示信息错误')
       contx=self.driver.find_element_by_id('content').get_attribute('value')
       self.assertTrue(u'代驾租车是由出租方提供车辆及驾驶人员的汽车租赁方式。' in contx,u'输入内容错误')

    def test_announcement_null2(self):
       '''
       公告内容错误，对比提示是否一致，不一致显示"提示信息错误"
       :return:
       '''
       self.driver.find_element_by_link_text(u'司机管理').click()
       self.driver.find_element_by_link_text(u'发布公告').click()
       self.driver.find_element_by_id('title').send_keys(u'代驾租车')
       self.driver.find_element_by_id('content').send_keys(u'')
       self.driver.find_element_by_id('noticeSubmit').click()
       tittx=self.driver.find_element_by_id('title').get_attribute('value')
       self.assertTrue(u'代驾租车' in tittx,u'输入内容错误')
       contx=self.driver.find_element_by_id('content_tip').text
       self.assertTrue(u'内容不能为空.' in contx,u'提示信息错误')

    # 发布成功
    def test_announcement_correct(self):
       '''
      成功发布公告信息
       :return:
       '''
       self.driver.find_element_by_link_text(u'司机管理').click()
       self.driver.find_element_by_link_text(u'发布公告').click()
       self.driver.find_element_by_id('title').send_keys(u'代驾租车')
       self.driver.find_element_by_id('content').send_keys(u'代驾租车是由出租方提供车辆及驾驶人员的汽车租赁方式。')
       tittx=self.driver.find_element_by_id('title').get_attribute('value')
       self.assertTrue(u'代驾租车' in tittx,u'输入内容错误')
       contx=self.driver.find_element_by_id('content').get_attribute('value')
       self.assertTrue(u'代驾租车是由出租方提供车辆及驾驶人员的汽车租赁方式。' in contx,u'输入内容错误')
       # 点击确定按钮
       self.driver.find_element_by_id('noticeSubmit').click()
       self.assertTrue(u'发布公告' in self.driver.title,u'界面跳转错误')
    # 取消
    def test_announcement_cancel(self):
       '''
       输入正确的公告信息取消
       :return:
       '''
       self.driver.find_element_by_link_text(u'司机管理').click()
       self.driver.find_element_by_link_text(u'发布公告').click()
       self.driver.find_element_by_id('title').send_keys(u'代驾租车')
       self.driver.find_element_by_id('content').send_keys(u'代驾租车是由出租方提供车辆及驾驶人员的汽车租赁方式。')
       tittx=self.driver.find_element_by_id('title').get_attribute('value')
       self.assertTrue(u'代驾租车' in tittx,u'输入内容错误')
       contx=self.driver.find_element_by_id('content').get_attribute('value')
       self.assertTrue(u'代驾租车是由出租方提供车辆及驾驶人员的汽车租赁方式。' in contx,u'输入内容错误')
       # 点击取消按钮
       self.driver.find_element_by_id('cancel').click()
       print self.driver.title
       self.assertTrue(u'司机管理/司机列表' in self.driver.title,u'界面跳转错误')



