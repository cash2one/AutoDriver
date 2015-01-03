# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import json
import urllib
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtNetwork
from framework.gui.ui import home_ui
import base

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeForm(QWidget, home_ui.Ui_Form):
    def __init__(self):
        super(HomeForm, self).__init__()

        self.setupUi(self)

        # self.http = QtNetwork.QHttp(parent=self)
        # # 绑定 done 信号
        # self.http.done.connect(self.on_req_done)
        # utf8_string = u'上海'.encode("utf-8")
        # shh = urllib.quote(utf8_string)
        # url_str = 'http://www.weather.com.cn/data/sk/101020100.html'
        # ur = u'http://api.map.baidu.com/telematics/v3/weather?location=上海&output=json&ak=3QaWoBGE8jWtBdIfl56yn582'
        #
        # self.url = QUrl(url_str)
        #
        # # 设置主机
        # self.http.setHost(self.url.host(), self.url.port(80))
        # self.getId = self.http.get(self.url.path())

        # self._cookiejar = QtNetwork.QNetworkCookieJar(parent=self)
        # self.manager = QtNetwork.QNetworkAccessManager(parent=self)
        # self.manager.setCookieJar(self._cookiejar)
        # self.manager.finished.connect(self.on_reply)
        #
        # self.req = QtNetwork.QNetworkRequest(
        #     QUrl("http://www.weather.com.cn/data/sk/101190101.html"))
        #
        # self.manager.get(self.req)
        if base.net!=None:
            base.net.finished.connect(self.on_reply)
            self.req = QtNetwork.QNetworkRequest(
                QUrl("http://www.weather.com.cn/data/sk/101190101.html"))
            base.net.get(self.req)

    def on_reply(self, reply):
        # print reply, self._cookiejar.allCookies()
        # print reply.rawHeaderList()
        #print reply.readAll()
        con = QString(reply.readAll())
        self.txt_a.setPlainText(con)
        reply.deleteLater() #待处理


    def on_req_done(self, error):
        if not error:
            print "Success"
            con = self.http.readAll()

            j_data = json.loads(str(QString(con).toLatin1()))
            weatherinfo=j_data['weatherinfo']
            c = weatherinfo['city']+u' 气温' +weatherinfo['temp']+ u'摄氏度'

            self.lbl_weather.setText(c)
        else:
            print "Error"