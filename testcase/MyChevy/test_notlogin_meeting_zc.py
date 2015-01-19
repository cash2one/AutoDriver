# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#未登录时点击活动报名弹出登录页面
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()


    def test_case(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_name(u'聚乐会').click()
        sleep(2)

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/imageView').click()
        sleep(2)

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/content_apply').click()#未登录点击报名进入登录页面
        self.driver.switch_to_alert()

       # print(self.driver.current_activity)
        self.assertEqual('.UserInformationActivity',self.driver.current_activity)

