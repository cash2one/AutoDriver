# coding=utf-8
__author__ = 'zhangchun'


from time import sleep
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()


    def test_case(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_name(u'保养预约维修').click()
        self.driver.switch_to_alert()#获取弹出框
        sleep(2)
        # els=self.driver.find_elements_by_class_name('android.widget.TextView')
        # txt=els[0].text.strip() 取第一个文本框的内容,strip()过滤空格
        # print txt
        # self.assertEqual(u'姓名',txt) 判断两个是否相等

        self.assertEqual('.UserInformationActivity',self.driver.current_activity)#判断当前页面是否为前面的信息
