# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#点击登录，检查性别选择框
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        sleep(2)
        self.driver.switch_to_alert()
        txt1=self.driver.find_elements_by_class_name('android.widget.TextView')[2].text
        txt2=self.driver.find_elements_by_class_name('android.widget.TextView')[3].text
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_woman')
        el.click()
        sleep(2)

        print txt1
        print txt2
        self.assertTrue(el.is_selected())