# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import time
import datetime
import re
from framework.core import box, data
from framework.util import sqlite

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtNetwork

from woodpecker.views import home_ui
from woodpecker.dialog import browser
from woodpecker.helpers import models


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

DOWNLOAD_SUCCESS = 0
LOAD_DATABASE = 1
DOWNLOAD_FAIL = 2
DB_PATH = PATH('./wp.db')


class HomeForm(QWidget, home_ui.Ui_Form):
    def __init__(self):
        super(HomeForm, self).__init__()

        self.setupUi(self)
        # self.dbm = self.data_handler()

        # self.nam = [self.netAccessNoCookie,self.netAccessNoCookie]#netAccess_method

        self.lbl_status.setText('Loading...')
        self.lbl_status.setFont(QFont("Microsoft YaHei", 11))
        self.connect(self.lbl_status, SIGNAL('linkActivated (const QString&)'), self.refresh_content)
        # self.connect(self, SIGNAL("loading_start()"), self.show_loading)
        # self.connect(self, SIGNAL("loading_finish()"), self.loading_finish)
        # self.lbl_colors = ['00a1f1', '7cbb00', 'ffbb00']
        # self.load_num = 0
        # self.loading_dlg=None
        # self.pages = ('http://www.ltesting.net/rss.xml', 'http://testerhome.com/topics/feedgood',
        # 'http://zaodula.com/feed')
        self.homepage = [{'title': u'领测软件测试网', 'url': 'http://www.ltesting.net/rss.xml'},
                         {'title': u'TesterHome社区精华帖', 'url': 'http://testerhome.com/topics/feedgood'},
                         {'title': u'互联网早读课', 'url': 'http://zaodula.com/feed'}]

        # 新闻更新时间段，这个时间段内已经更新过，则只能通过点击刷新加载
        self.time_ranges = ['2015-2-2 9:00:00.0', '2015-2-2 11:00:00.0', '2015-2-2 13:00:00.0', '2015-2-2 15:00:00.0',
                            '2015-2-2 17:00:00.0']

        self.nam_finish_num = 0  # 页面加载累加次数

        # 指定时间段刷新
        self.dbm = self.data_handler()
        if self.update_refresh_time(self.dbm):
            self.dbm.clean_table('News')
            self.start_load_page()
        else:
            for hp in self.homepage:
                news_ = self.dbm.fetchall('select * from News where Category="%s"' % hp['title'])
                lis = ''
                for new in news_:
                    aStyle = 'text-decoration:none'
                    liStyle = 'line-height:23px;'
                    li = "<li style=%s><a href=%s style=%s>%s</a></li>" % (liStyle, new[3], aStyle, new[1])
                    lis += li
                self.load_to_ul(lis, hp['title'], LOAD_DATABASE)


    def data_handler(self):
        if not os.path.exists(DB_PATH):
            db = data.generateData(DB_PATH)
            db.init_table(models.sql())

        return sqlite.DBManager(DB_PATH)


    def netAccess(self, url, reply_func):
        m = QtNetwork.QNetworkAccessManager(self)
        # m1.setCookieJar(ja.cookie)
        m.finished.connect(reply_func)
        req = QtNetwork.QNetworkRequest(QUrl(url))
        req.setRawHeader("User-Agent",
                         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")
        req.setRawHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        # req.setRawHeader("Accept-Language", "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4")
        # req.setRawHeader("Accept-Encoding", "deflate")
        # req.setRawHeader("Accept-Charset", "utf-8;q=0.7,*;q=0.7")
        # req.setRawHeader("Connection", "keep-alive")
        # req.setRawHeader("Accept-Encoding", "gzip, deflate, sdch")
        m.get(req)

    def start_load_page(self):
        self.netAccess(self.homepage[0]['url'], self.on_one_reply)
        # 这个网站加载速度较慢，所以单独来加载
        self.netAccess(self.homepage[2]['url'], self.on_three_reply)

    def on_one_reply(self, reply):
        title = self.homepage[0]['title']
        if reply.error() == reply.NoError:
            self.load_to_ul(reply.readAll(), title, DOWNLOAD_SUCCESS)
            # 加载完成后，再次加载下一个页面
            self.netAccess(self.homepage[1]['url'], self.on_two_reply)
        else:
            self.load_to_ul('', title, DOWNLOAD_FAIL)


    def on_two_reply(self, reply):
        title = self.homepage[1]['title']
        if reply.error() == reply.NoError:
            self.load_to_ul(reply.readAll(), title, DOWNLOAD_SUCCESS)
        else:
            self.load_to_ul('', title, DOWNLOAD_FAIL)


    def on_three_reply(self, reply):
        title = self.homepage[2]['title']
        if reply.error() == reply.NoError:
            self.load_to_ul(reply.readAll(), title, DOWNLOAD_SUCCESS)
        else:
            self.load_to_ul('', title, DOWNLOAD_FAIL)


    def refresh_content(self, txt):
        # 初始化
        self.lbl_status.setText(u"Loading...")
        self.dbm = self.data_handler()
        self.dbm.clean_table('News')
        self.nam_finish_num = 0
        # 清除原先加载的Label
        for i in reversed(range(0, self.hz_layout.count())):
            self.hz_layout.itemAt(i).widget().deleteLater()
            self.hz_layout.itemAt(i).widget().setParent(None)

        self.start_load_page()

    def clearLayout(self, layout):
        if layout is not None:
            old_layout = layout
            for i in reversed(range(old_layout.count())):
                old_layout.itemAt(i).widget().setParent(None)
            import sip

            sip.delete(old_layout)


    def open_file_browser(self, txt):
        fileBrowser = browser.FileDialog(txt, 2, self.netAccessNoCookie)
        fileBrowser.exec_()

    def load_to_ul(self, content, title, download_status):
        lbl = QLabel()
        lbl.setAlignment(Qt.AlignTop)
        lbl.setStyleSheet("background-color:#ffffff;padding:20px 15px 0 15px;font-family:Microsoft YaHei")
        lbl.setMinimumWidth(350)
        lbl.setMaximumHeight(430)
        # lbl.setOpenExternalLinks(True)#在浏览器中打开链接

        if download_status == DOWNLOAD_SUCCESS:
            # 解析xml，并存入数据库
            result = self.parse_xml_to_db(title, content)
            lbl.setText(u"<h3>%s</h3><ul>%s</ul>" % (title, result))
            # self.save_home_data(title, result, time_str)
        elif download_status == LOAD_DATABASE:
            lbl.setText(u"<h3>%s</h3><ul>%s</ul>" % (title, content))
        elif download_status == DOWNLOAD_FAIL:
            lbl.setText(u"<h3>%s</h3><ul>%s</ul>" % (title, u'<li>加载失败</li>'))
            # self.save_home_data(title, u'<li>加载失败</li>', time_str)

        self.hz_layout.addWidget(lbl)

        # Label中的链接点击信号槽
        self.connect(lbl, SIGNAL('linkActivated (const QString&)'), self.open_file_browser)
        self.nam_finish_num += 1
        if self.nam_finish_num >= len(self.homepage):
            self.lbl_status.setText(u"测试网站动态更新内容 [<a href='refresh()'>刷新</a>]")
            self.emit(SIGNAL("loading_finish()"))
            self.dbm.close_db()


    def parse_xml_to_db(self, cat, xml_string):
        from xml.etree import cElementTree

        datas = []

        lis = ''
        per = cElementTree.fromstring(xml_string)
        root = per.findall('channel')
        # for child in root:
        items = root[0].findall('item')
        item_num = 0

        aStyle = 'text-decoration:none'
        liStyle = 'line-height:23px;'
        for item in items:
            txt = item.find('title').text
            link = item.find('link').text
            if not u'招聘' in txt and not u'薪' in txt:
                if 'zaodula.com' in link:
                    # 屏蔽早读列表带的日期
                    pattern = re.compile(r'-\d+')
                    match = pattern.search(txt)
                    if match:
                        zd_index = txt.find(match.group())
                        txt = txt[0:zd_index]

                data = (txt, cat, link, datetime.datetime.now())
                datas.append(data)
                li = "<li style=%s><a href=%s style=%s>%s</a></li>" % (liStyle, link, aStyle, txt)
                lis += li
                item_num += 1
            if item_num >= 15:
                break

        self.dbm.insert_values("INSERT INTO News values (NULL,?,?,?,?)", datas)
        return lis


    def netAccessNoCookie(self, api, reply_func):
        m = QtNetwork.QNetworkAccessManager(self)
        # m1.setCookieJar(ja.cookie)
        m.finished.connect(reply_func)
        req = QtNetwork.QNetworkRequest(QUrl(api))
        # req.setRawHeader("Host", "www.nuihq.com")
        req.setRawHeader("User-Agent",
                         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")
        req.setRawHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.setRawHeader("Accept-Language", "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4")
        # req.setRawHeader("Accept-Encoding", "deflate")
        # req.setRawHeader("Accept-Charset", "utf-8;q=0.7,*;q=0.7")
        # req.setRawHeader("Connection", "keep-alive")
        # req.setRawHeader("Accept-Encoding", "gzip, deflate, sdch")
        m.get(req)

    def get_time_stamp(self, time_str):
        return time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f'))

    def get_recent_time(self):
        max_time_str = '2000-2-1 9:00:00.0'
        for t in self.time_ranges:
            t1 = self.get_time_stamp(max_time_str) - time.time()
            t2 = self.get_time_stamp(t) - time.time()

            if t2 < 0 and t1 < t2:
                max_time_str = t

        return self.get_time_stamp(max_time_str)

    def update_refresh_time(self, dbm):
        # d1 = datetime.datetime.now()
        # d3 = d1 + datetime.timedelta(days=10)
        # t3 = d1 - datetime.timedelta(minutes=30)
        isRefresh = False

        d = dbm.fetchone('select * from News')
        if d is None:
            return True
        # 获取数据库最新的一条数据，与最近的时间段比较
        if (self.get_time_stamp(str(d[-1])) - self.get_recent_time()) < 0:
            isRefresh = True

        return isRefresh


