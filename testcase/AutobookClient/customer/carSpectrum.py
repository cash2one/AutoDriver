# coding=utf-8
__author__ = 'wangsahnshan@126.com'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    用户登录，查看关于车谱
    '''
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_carSpectrum(self):
       '''
       关于车谱界面的：客服电话
       :return:
       '''

       current_activity = self.driver.current_activity
       #点击进入使用
       # self.driver.find_id('start_btn').click()
       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #点击关于车谱
       self.driver.find_ids('person_item')[4].click()
       #对比
       text=self.driver.find_id('tv_title_text').text
       print text
       self.assertTrue(u'关于车谱' in text,'msg')

       #点击客服电话连接
       self.driver.find_id('tv_phonenumber').click()
       # phone=self.driver.find_id('digits').text
       # self.assertTrue(u'4009204358' in phone ,'msg')

    def test_email(self):
       '''
       关于车谱界面的：客服邮箱
       :return:
       '''
       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #点击关于车谱
       self.driver.find_ids('person_item')[4].click()

       #点击客服邮箱连接
       self.driver.find_id('tv_email').click()
       # email=self.driver.find_id('alertTitle').text
       # print email
       # self.assertTrue(u'电子邮件' in email ,'msg')
       # #点击取消按钮，返回到关于车谱界面
       # self.driver.find_id('button2').click()


    def test_weibo(self):
       '''
        关于车谱界面的：官方微博
        :return:
       '''
       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #点击关于车谱
       self.driver.find_ids('person_item')[4].click()
       #点击官方微博“车谱”
       self.driver.find_id('tv_weibo').click()

       # tv_weibo=self.driver.find_id('sbrowser_url_bar').text
       # self.assertTrue(u'm.weibo.cn/d/automobilebook?jumpfrom=weibocom' in tv_weibo ,'msg')
       # self.driver.find_id('').click()

    def test_web(self):
       '''
       关于车谱界面的：官方网站
       :return:
       '''
       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #点击关于车谱
       self.driver.find_ids('person_item')[4].click()
       #点击官方网站
       self.driver.find_id('tv_web').click()
       # tv_web=self.driver.find_id('sbrowser_url_bar').text
       # self.assertTrue(u'www.automobilebook.cn/wap/' in tv_web ,'msg')
       # self.driver.find_id('').click()

       #点击左上角返回按钮
       # self.driver.find_id('button_title_back').click()

