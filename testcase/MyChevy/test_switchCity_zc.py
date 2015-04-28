# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#点击城市切换按钮，进入城市列表
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_party').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/rl_city').click()
        table=self.driver.current_activity
        sleep(3)
        # self.driver.find_elements_by_class_name('android.view.View')[0].find_element_by_name('B').click()
        # txt=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/catalog').text
        el=self.driver.find_elements_by_class_name('android.widget.TextView')[5]
        text1=el.text
        el.click()
        sleep(3)
        text2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_cityName').text

        self.assertEqual(table,'.SelectCityActivity')
        #点击切换城市按钮，进入城市列表页面
        # self.assertEqual('B',txt)
        #点击字母B，跳转到B开头的城市
        self.assertEqual(text1,text2)
        #点击某个城市，切换到该城市