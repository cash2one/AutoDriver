# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import time
import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtNetwork
from framework.gui.views import home_ui
from framework.gui.dialog import browser,loading
from framework.core import the


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeForm(QWidget, home_ui.Ui_Form):
    def __init__(self, netAccess_method):
        super(HomeForm, self).__init__()

        self.setupUi(self)
        self.nam = netAccess_method
        self.lbl_status.setText('Loading...')
        self.lbl_status.setFont(QFont("Microsoft YaHei", 11))
        self.connect(self.lbl_status, SIGNAL('linkActivated (const QString&)'), self.refresh_content)
        # self.connect(self, SIGNAL("loading_start()"), self.show_loading)
        # self.connect(self, SIGNAL("loading_finish()"), self.loading_finish)
        # self.lbl_colors = ['00a1f1', '7cbb00', 'ffbb00']
        # self.load_num = 0
        #self.loading_dlg=None

        if len(the.jira.home) >= 3:
            time_str = ''
            for dic in the.jira.home:
                title = dic['title']
                result = dic['result']
                time_str = dic['time']
                self.load_to_ul(result, title, time_str, False)
            self.lbl_status.setText(u"测试网站动态更新内容 %s [<a href='refresh()'>刷新</a>]" % time_str)

        else:
            self.nam('http://www.ltesting.net/rss.xml', self.on_ltesting_reply)
            self.emit(SIGNAL("loading_start()"))

    def on_ltesting_reply(self, reply):
        if reply.error() == reply.NoError:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            self.load_to_ul(reply.readAll(), u'领测软件测试网', time_str, True)
            self.nam('http://testerhome.com/topics/feedgood', self.on_testerhome_reply)


    def on_testerhome_reply(self, reply):
        if reply.error() == reply.NoError:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            self.load_to_ul(reply.readAll(), u'TesterHome社区精华帖', time_str, True)
            self.nam('http://zaodula.com/feed', self.on_zaodula_reply)

    def on_zaodula_reply(self, reply):
        if reply.error() == reply.NoError:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            self.load_to_ul(reply.readAll(), u'互联网早读课', time_str, True)

            self.lbl_status.setText(u"测试网站动态更新内容 %s [<a href='refresh()'>刷新</a>]" % time_str)
            self.emit(SIGNAL("loading_finish()"))


    def refresh_content(self, txt):
        # self.load_num = 0
        self.lbl_status.setText(u"Loading...")
        the.jira.home = []
        # self.clearLayout(self.hz_layout)
        for i in reversed(range(0, self.hz_layout.count())):
            self.hz_layout.itemAt(i).widget().deleteLater()
            self.hz_layout.itemAt(i).widget().setParent(None)

        # self.hz_layout.setContentsMargins(0,0,0,0)
        # for lbl in self.lbls:
        # #lbl.setParent(None)
        # self.hz_layout.removeWidget(lbl)
        #     self.hz_layout.setContentsMargins(0,0,0,0)
        #     lbl.deleteLater()
        #     #lbl = None
        self.nam('http://www.ltesting.net/rss.xml', self.on_ltesting_reply)

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

    def load_to_ul(self, content, title, time_str, isDownload):
        lbl = QLabel()
        lbl.setAlignment(Qt.AlignTop)
        lbl.setStyleSheet("background-color:#ffffff;padding:20px 15px 0 15px;font-family:Microsoft YaHei")
        lbl.setMinimumWidth(350)
        lbl.setMaximumHeight(430)
        # lbl.setOpenExternalLinks(True)
        result = content
        if isDownload:
            result = self.read_xml_feed(content)
            self.save_home_data(title, result, time_str)

        # bg_color = self.lbl_colors[self.load_num]
        lbl.setText(u"<h3>%s</h3><ul>%s</ul>" % (title, result))
        self.hz_layout.addWidget(lbl)
        self.connect(lbl, SIGNAL('linkActivated (const QString&)'), self.open_file_browser)
        #self.load_num += 1

    def save_home_data(self, title, result, time_str):
        res_dict = {}
        res_dict['title'] = title
        res_dict['result'] = result
        res_dict['time'] = time_str
        the.jira.home.append(res_dict)


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
    #     self.loading_dlg = loading.LoadingDialog()
    #     self.loading_dlg.exec_()
    #
    # def loading_finish(self):
    #     self.loading_dlg.destroy()

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



