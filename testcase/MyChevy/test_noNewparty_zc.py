# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#切换没有最新活动的城市，页面显示暂时无最新活动
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_name(u'聚乐会').click()
        sleep(10)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/rl_city').click()
        sleep(3)
        for i in range(0, 5):
            #定位元素的原位置
            origin_el =self.driver.find_elements_by_class_name('android.widget.TextView')[3]
            #定位元素要移动到的目标位置
            destination_el =self.driver.find_elements_by_class_name('android.widget.TextView')[0]
            #执行元素的移动操作
            self.driver.drag_and_drop(origin_el,destination_el)
        self.driver.find_element_by_name(u'安康').click()
        text1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_no_newparty').text
        self.assertEqual(u'暂时没有最新活动',text1)

