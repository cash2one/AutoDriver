# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import time
import re
from framework.core import box

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtNetwork

from woodpecker.views import home_ui
from woodpecker.dialog import browser


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

DOWNLOAD_SUCCESS = 0
DOWNLOAD_MEMORY = 1
DOWNLOAD_FAIL = 2


class HomeForm(QWidget, home_ui.Ui_Form):
    def __init__(self):
        super(HomeForm, self).__init__()

        self.setupUi(self)
        #self.nam = [self.netAccessNoCookie,self.netAccessNoCookie]#netAccess_method
        self.lbl_status.setText('Loading...')
        self.lbl_status.setFont(QFont("Microsoft YaHei", 11))
        self.connect(self.lbl_status, SIGNAL('linkActivated (const QString&)'), self.refresh_content)
        # self.connect(self, SIGNAL("loading_start()"), self.show_loading)
        # self.connect(self, SIGNAL("loading_finish()"), self.loading_finish)
        # self.lbl_colors = ['00a1f1', '7cbb00', 'ffbb00']
        # self.load_num = 0
        # self.loading_dlg=None
        self.pages = ('http://www.ltesting.net/rss.xml', 'http://testerhome.com/topics/feedgood',
                      'http://zaodula.com/feed')
        self.nam_finish_num = 0

        if len(box.jira.home) >= len(self.pages):
            for dic in box.jira.home:
                self.nam_finish_num += 1
                title = dic['title']
                result = dic['result']
                time_str = dic['time']
                self.load_to_ul(result, title, time_str, DOWNLOAD_MEMORY)
        else:
            self.start_load_page()

    def netAccess(self, url, reply_func):
        m = QtNetwork.QNetworkAccessManager(self)
        # m1.setCookieJar(ja.cookie)
        m.finished.connect(reply_func)
        req = QtNetwork.QNetworkRequest(QUrl(url))
        # req.setRawHeader("Host", "www.nuihq.com")
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
        self.netAccess(self.pages[0], self.on_one_reply)
        # 这个网站加载速度较慢，所以单独来加载
        self.netAccess(self.pages[2], self.on_three_reply)

    def on_one_reply(self, reply):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        title = u'领测软件测试网'
        if reply.error() == reply.NoError:
            self.load_to_ul(reply.readAll(), title, time_str, DOWNLOAD_SUCCESS)
            # 加载完成后，再次加载下一个页面
            self.netAccess(self.pages[1], self.on_two_reply)
        else:
            self.load_to_ul('', title, time_str, DOWNLOAD_FAIL)


    def on_two_reply(self, reply):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        title = u'TesterHome社区精华帖'
        if reply.error() == reply.NoError:
            self.load_to_ul(reply.readAll(), title, time_str, DOWNLOAD_SUCCESS)
        else:
            self.load_to_ul('', title, time_str, DOWNLOAD_FAIL)


    def on_three_reply(self, reply):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        title = u'互联网早读课'
        if reply.error() == reply.NoError:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            self.load_to_ul(reply.readAll(), title, time_str, DOWNLOAD_SUCCESS)
        else:
            self.load_to_ul('', title, time_str, DOWNLOAD_FAIL)


    def refresh_content(self, txt):
        # 初始化
        self.lbl_status.setText(u"Loading...")
        box.jira.home = []
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

    def load_to_ul(self, content, title, time_str, download_status):
        lbl = QLabel()
        lbl.setAlignment(Qt.AlignTop)
        lbl.setStyleSheet("background-color:#ffffff;padding:20px 15px 0 15px;font-family:Microsoft YaHei")
        lbl.setMinimumWidth(350)
        lbl.setMaximumHeight(430)
        # lbl.setOpenExternalLinks(True)#在浏览器中打开链接

        if download_status == DOWNLOAD_SUCCESS:
            result = self.read_xml_feed(content)
            lbl.setText(u"<h3>%s</h3><ul>%s</ul>" % (title, result))
            self.save_home_data(title, result, time_str)
        elif download_status == DOWNLOAD_MEMORY:
            lbl.setText(u"<h3>%s</h3><ul>%s</ul>" % (title, content))
        elif download_status == DOWNLOAD_FAIL:
            lbl.setText(u"<h3>%s</h3><ul>%s</ul>" % (title, u'<li>加载失败</li>'))
            self.save_home_data(title, u'<li>加载失败</li>', time_str)

        self.hz_layout.addWidget(lbl)

        # Label中的链接点击信号槽
        self.connect(lbl, SIGNAL('linkActivated (const QString&)'), self.open_file_browser)
        self.nam_finish_num += 1
        if self.nam_finish_num >= len(self.pages):
            self.lbl_status.setText(u"测试网站动态更新内容 %s [<a href='refresh()'>刷新</a>]" % time_str)
            self.emit(SIGNAL("loading_finish()"))

    def save_home_data(self, title, result, time_str):
        res_dict = {}
        res_dict['title'] = title
        res_dict['result'] = result
        res_dict['time'] = time_str
        box.jira.home.append(res_dict)


    def read_xml_feed(self, xml_string):
        from xml.etree import cElementTree

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

                li = "<li style=%s><a href=%s style=%s>%s</a></li>" % (liStyle, link, aStyle, txt)
                lis += li
                item_num += 1
            if item_num >= 15:
                break
        return lis

    # def show_loading(self):
    # self.loading_dlg = loading.LoadingDialog()
    # self.loading_dlg.exec_()
    #
    # def loading_finish(self):
    # self.loading_dlg.destroy()

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



