# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import time
import re
from drivers import *


class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.p_list = ['ats', 'atsl']

        self.car = []


    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_dd(self):
        time.sleep(1)
        listImgs = self.driver.find_id('ATS').find_class('configure').get_attribute('innerHTML')
        self.filter_content(listImgs)

    def filter_content(self, txt):
        start_table = txt.find('<div class="listImg">')
        end_table = txt.find('</table>') + len('</table>')
        table_str = txt[start_table:end_table]
        self.car.append(table_str)

        txt_ = txt[end_table:]

        if txt_.find('<div class="listImg">') >= 0:
            self.filter_content(txt_)

    def filter_table(self, table_str):
        start_em = table_str.find('<em>')
        end_em = table_str.find('</em>')
        em = table_str[start_em:end_em]

        dict_str = {}
        dict_str['h6'] = em
        tr = ()
        start_tr = table_str.find('<tr>')
        end_tr = table_str.find('</tr>')
        tr = table_str[start_tr:end_tr]

