# coding=utf-8
__author__ = 'guguohai@outlook.com'


from PyQt4 import QtGui, QtCore, QtNetwork


class MainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self._cookiejar = QtNetwork.QNetworkCookieJar(parent=self)
        self.manager = QtNetwork.QNetworkAccessManager(parent=self)

        self.manager.setCookieJar(self._cookiejar)
        self.manager.finished.connect(self.on_reply)

        self.req = QtNetwork.QNetworkRequest(
            QtCore.QUrl("http://www.testwo.com/user/login?referer=none&name=haio&password=ggh019466&captcha=bfa7"))

        self.manager.get(self.req)

    def on_reply(self, reply):
        print reply, self._cookiejar.allCookies()
        print reply.rawHeaderList()
        # print reply.readAll()


if __name__ == "__main__":
    app = QtGui.QApplication([])
    widget = MainWidget()
    widget.show()
    app.exec_()