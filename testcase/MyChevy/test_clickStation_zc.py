# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#点击24小时服务站进入服务站查询页面
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(5)
        for i in range(0,12):#以下操作连续12次
        #定位元素的原位置
            origin_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[0]
        #定位元素要移动到的目标位置
            destination_el =self.driver.find_elements_by_class_name("android.widget.LinearLayout")[3]
        #执行元素的移动操作
            self.driver.drag_and_drop(origin_el,destination_el)

        self.assertEqual('.StationActivity',self.driver.current_activity)