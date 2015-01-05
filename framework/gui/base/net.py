# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4 import QtCore, QtNetwork


class NetManager():
    def __init__(self):
        self.host = 'http://192.168.3.11:8080'
        # self.manager = QtNetwork.QNetworkAccessManager(parent=self)
        # self.manager.setCookieJar(self.cookie_jar)
        # self.manager.finished.connect(self.on_reply)
        #
        # self.req = QtNetwork.QNetworkRequest(
        # QtCore.QUrl("http://www.testwo.com/user/login?referer=none&name=haio&password=ggh019466&captcha=bfa7"))
        #
        # self.manager.get(self.req)
        # self.cookie_jar = None

    # def cookie(self, parent):
    # self.cookie_jar = QtNetwork.QNetworkCookieJar(parent)


    def get(self, parent, cookie, api, reply_func):
        manager = QtNetwork.QNetworkAccessManager(parent)
        manager.setCookieJar(cookie)
        manager.finished.connect(reply_func)

        req = QtNetwork.QNetworkRequest(QtCore.QUrl(self.host + api))
        manager.get(req)
        return manager

    def load(self, reply):
        if reply.error() == reply.NoError:
            pass