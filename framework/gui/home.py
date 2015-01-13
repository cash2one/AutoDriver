# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import re
import json
import urllib
import operator
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtNetwork
from PyQt4.QtNetwork import QNetworkRequest
from framework.gui.views import home_ui
from framework.gui.dialog import browser
from framework.util import fs


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeForm(QWidget, home_ui.Ui_Form):
    def __init__(self, netAccess_method):
        super(HomeForm, self).__init__()

        self.setupUi(self)
        self.nam = netAccess_method
        # self.http = QtNetwork.QHttp(self)
        # # 绑定 done 信号
        # self.http.done.connect(self.on_req_done)
        # # utf8_string = u'上海'.encode("utf-8")
        # #shh = urllib.quote(utf8_string)
        # url_str = 'http://www.51testing.com/html/index.html'
        # #url_str='http://testerhome.com/topics/feedgood'
        # #url_str = 'http://www.weather.com.cn/data/sk/101020100.html'
        # #ur = u'http://api.map.baidu.com/telematics/v3/weather?location=上海&output=json&ak=3QaWoBGE8jWtBdIfl56yn582'
        #
        # self.url = QUrl(url_str)
        #
        # # 设置主机
        # self.http.setHost(self.url.host(), self.url.port(80))
        # self.getId = self.http.get(self.url.path())
        # self.nam('http://www.51testing.com/html/index.html', self.on_51testing_reply)
        self.lbl_status.setText('Loading...')
        self.lbl_status.setFont(QFont("Microsoft YaHei", 11))

        self.nam('http://www.51testing.com/html/31/category-catid-31.html', self.on_51testing_reply)


    def on_51testing_reply(self, reply):
        if reply.error() == reply.NoError:
            codec = QTextCodec.codecForName("GBK")
            con = unicode(codec.toUnicode(reply.readAll()))

            lis = self.news_51t(con)  # + self.blog_51t(con)

            lbl = QLabel()
            # lbl.setOpenExternalLinks(True)
            lbl.setText(u"<h3>51Testing最新更新</h3><ul>%s</ul>" % lis)
            self.hz_layout.addWidget(lbl)
            self.connect(lbl, SIGNAL('linkActivated (const QString&)'), self.open_file_browser)

            self.nam('http://testerhome.com/topics/feedgood', self.on_testerhome_reply)
        else:
            print reply.error()

    def open_file_browser(self, txt):
        fileBrowser = browser.FileDialog(txt,2,self.netAccessNoCookie)
        fileBrowser.exec_()

    def news_51t(self, con):
        # start_str = '<ul class="msglist" style="padding-bottom:2px;">'
        start_str = '<ul class="lie2"><!--zjbw-->'
        start_idx = con.find(start_str) + len(start_str)

        start_con = con[start_idx:len(con)]
        end_idx = start_con.find('</ul>')
        result = start_con[0:end_idx]

        p = re.compile(r'<a.+?href=.+?>.+?</a>')

        lis = ''
        hrefs = p.findall(result)
        for i in range(0, len(hrefs)):
            if i % 2 != 0 and not u'招聘' in hrefs[i]:
                title_start = hrefs[i].find('title="') + len('title="')
                title_con = hrefs[i][title_start:len(hrefs[i])]
                title_end = title_con.find('"')
                title = title_con[0:title_end]

                href_start = hrefs[i].find('href="') + len('href="')
                href_con = hrefs[i][href_start:len(hrefs[i])]
                href_end = href_con.find('"')
                href = href_con[0:href_end]

                lis += "<li style='line-height:22px;'><a href=%s>%s</a></li>" % (href, title)

        return lis

    # def blog_51t(self, con):
    # blog_s = u'博客最新热文'
    # start_idx1 = con.find(blog_s) + len(blog_s)
    # start_con1 = con[start_idx1:len(con)]
    #     blog_ss = '<div class="msgtitlelist">'
    #     start_idx2 = con.find(start_con1) + len(blog_ss)
    #     start_con = con[start_idx2:len(con)]
    #     end_idx = start_con.find('</ul>')
    #     result = start_con[0:end_idx].replace('<ul>', '')
    #     p = re.compile(r'<a.+?href=.+?>.+?</a>')
    #     hrefs = p.findall(result)
    #     lis = ''
    #     for i in range(0, len(hrefs)):
    #         if i % 2 != 0 and not u'招聘' in hrefs[i]:
    #             lis += "<li style='line-height:22px;'>" + hrefs[i].replace(u'(图)', '') + "</li>"
    #     return lis

    def on_testerhome_reply(self, reply):
        if reply.error() == reply.NoError:
            result = self.read_xml_feed(reply.readAll())
            lbl = QLabel()
            #lbl.setOpenExternalLinks(True)
            lbl.setText(u"<h3>TesterHome社区精华帖</h3><ul>%s</ul>" % result)
            self.hz_layout.addWidget(lbl)
            self.connect(lbl, SIGNAL('linkActivated (const QString&)'), self.open_file_browser)

            #http://zaodula.com/feed
            self.nam('http://zaodula.com/feed', self.on_zaodula_reply)

    def on_zaodula_reply(self, reply):
        if reply.error() == reply.NoError:
            result = self.read_xml_feed(reply.readAll())

            lbl = QLabel()
            #lbl.setOpenExternalLinks(True)
            lbl.setText(u"<h3>互联网的早读课</h3><ul>%s</ul>" % result)
            self.hz_layout.addWidget(lbl)
            self.connect(lbl, SIGNAL('linkActivated (const QString&)'), self.open_file_browser)
            self.lbl_status.setText('')



    def read_xml_feed(self, xml_string):
        from xml.etree import cElementTree

        lis = ''
        per = cElementTree.fromstring(xml_string)
        root = per.findall('channel')
        # for child in root:
        items = root[0].findall('item')
        item_num = 0
        for item in items:
            txt = item.find('title').text
            link = item.find('link').text
            if not u'招聘' in txt:
                li = "<li style='line-height:22px;'><a href='%s'>%s</a></li>" % (link, txt)
                lis += li
                item_num += 1
            if item_num >= 15:
                break
        return lis


    def netAccessNoCookie(self, api, reply_func):
        m = QtNetwork.QNetworkAccessManager(self)
        #m1.setCookieJar(ja.cookie)
        m.finished.connect(reply_func)
        req = QtNetwork.QNetworkRequest(QUrl(api))
        req.setHeader(QNetworkRequest.ContentTypeHeader, QVariant("text/html; charset=utf-8"))
        m.get(req)



