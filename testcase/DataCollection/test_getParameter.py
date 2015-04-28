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

        self.cars = (
            ('ats', 'ATS'), ('atsl', 'ATSL'), ('cts', 'CTS'), ('coupe', 'COUPE'), ('vcts', 'VCTS'),
            ('vcoupe', 'VCOUPE'), ('xts', 'XTS'), ('srx', 'SRX'), ('escalade', 'Escalade'),
            ('esv', 'Escalade-esv'))
        #http://t3.pro-trend.com.cn/New_web/ATS_enjoy/facade_1.jpg ATS
        #http://t3.pro-trend.com.cn/New_web/mainbody/xts/facade_1.jpg XTS
        #http://t3.pro-trend.com.cn/New_web/mainbody/vcts/facade_1.jpg CTS-V
        self.cdi_url = 'http://www.cadillac.com.cn/public_parameter.html?model='

        self.wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
        self.sheet = None
        self.row_num = 0


    def tearDown(self):
        try:
            path = os.path.join(PATH('./'), 'cadillac.xls')
            self.wbk.save(path)
        except IOError:
            print u'excel is open.'
            # self.driver.switch_to_home()

    def test_cadillac(self):
        # setUp self.app() 时,已经预先访问了drops[0]
        # self.sheet = self.wbk.add_sheet(self.cars[0][1], cell_overwrite_ok=True)
        # self.find_one()

        lis = self.driver.find_class('tag_options').find_tags('li')
        for i in range(1, len(lis)):
        # if 'open_selected' in lis[i].get_attribute('class') and i < len(lis) - 1:
            drops = self.cars[i]
            self.driver.get(self.cdi_url + drops[0])
            self.sheet = self.wbk.add_sheet(drops[1], cell_overwrite_ok=True)
            self.row_num = 0
            self.find_one()
            time.sleep(0.5)

    def find_one(self):
        concents = self.driver.find_class('carbuying').find_classes('concent')
        ats = None
        for con in concents:
            if 'block' in con.get_attribute('style'):
                ats = con
                break

        title_configure = ats.find_class('title_configure').get_attribute('innerHTML')
        configure = ats.find_class('configure').get_attribute('innerHTML')

        rr = re.compile(r'(?<=<th>).*?(?=</th>)')
        header = rr.findall(title_configure)
        for col_index in range(0, len(header)):
            self.sheet.write(self.row_num, col_index + 1, header[col_index])
        self.row_num += 1


        self.filter_write_content(configure)


    def filter_write_content(self, txt):
        # start_table = txt.find('<table')
        # end_table = txt.find('</table>') + len('</table>')
        # table_str = txt[start_table:end_table]

        tables = re.findall(r'<div class="listImg">.*?</table>', txt, re.DOTALL)

        for table in tables:

            re_symbol = re.compile(r'(?<=<em>).*?(?=</em>)')
            match = re_symbol.search(table)
            if match:
                self.sheet.write(self.row_num, 0, match.group())
                self.row_num += 1

            self.re_table(table)

            # txt_ = txt[end_table:]
            #
            # if txt_.find('<div class="listImg">') >= 0:
            # self.filter_write_content(txt_)

    def re_table(self, html_str):
        trs = re.findall(r'<tr>.*?</tr>', html_str, re.DOTALL)
        for tr in trs:
            trc = tr.replace('&nbsp;', '')

            x = re.findall(r'>([^<>]*)(?:</p>)?</td>', trc, re.DOTALL)  # </p>
            x = map(lambda s: s.strip(), x)

            for col_index in range(0, len(x)):
                self.sheet.write(self.row_num, col_index, x[col_index])
            self.row_num += 1

