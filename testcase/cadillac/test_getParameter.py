# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import re
import xlwt
from drivers import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


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

        self.write_xls(self.car)

    def filter_content(self, txt):
        start_table = txt.find('<div class="listImg">')
        end_table = txt.find('</table>') + len('</table>')
        table_str = txt[start_table:end_table]

        table_list= self.table_to_list(table_str)
        self.car.append(table_list)


        txt_ = txt[end_table:]

        if txt_.find('<div class="listImg">') >= 0:
            self.filter_content(txt_)

    # def filter_table(self, table_str):
    # start_em = table_str.find('<em>')
    # end_em = table_str.find('</em>')
    #     em = table_str[start_em:end_em]
    #
    #     dict_str = {}
    #     dict_str['h6'] = em
    #
    #     start_tr = table_str.find('<tr>')
    #     end_tr = table_str.find('</tr>')
    #     tr = table_str[start_tr:end_tr]

    def table_to_list(self, html_str):
        trs = re.findall(r'<tr>.*?</tr>', html_str, re.DOTALL)
        rows = []
        for tr in trs:
            x = re.findall(r'>([^<>]*)(?:</a>)?</td>', tr, re.DOTALL)
            x = map(lambda s: s.strip(), x)
            rows.append(x)
        return rows

    def write_xls(self, datas):
        report_path = PATH('./')
        file_name = 'wwee'

        wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = wbk.add_sheet('sheet', cell_overwrite_ok=True)

        # title = ['id', 'CPU(%)', 'Memory(MB)', 'Net1_sent', 'Net1_recv', 'Net2_sent', 'Net2_recv', 'UpdateTime']
        # t_index = 0
        # for t in title:
        #     sheet.write(0, t_index, t)
        #     t_index += 1

        row_num = 0
        for data in datas:
            for row_index in range(0, len(data)):
                for col_index in range(0, len(data[row_index])):
                    sheet.write(row_num, col_index, data[row_index][col_index])
                row_num += 1

            sheet.write(row_num, 0, 'gewgwgwegwegwe')

        try:
            path = os.path.join(report_path, '%s.xls' % file_name)
            wbk.save(path)
        except IOError:
            print u'excel is open.'

        return file_name + '.xls'
