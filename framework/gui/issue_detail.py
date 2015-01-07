# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import issue_detail_ui
from framework.util import convert
from framework.gui.base import *
import file_browser
from PyQt4 import QtNetwork


class IssueDialog(QDialog, issue_detail_ui.Ui_Dialog):
    def __init__(self, data=None):
        QDialog.__init__(self)

        self.data = data

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
        self.lbl_title.setWordWrap(True)

        self.atts = []
        self.atts_index = 0

        # self.net_manager = net.NetManager(jira.cookie, self)
        if data != None:
            # self.net_manager.get(data['self'], self.on_reply)
            self.load_data_to_ui(data)

            # manager = QtNetwork.QNetworkAccessManager(self)
            # manager.setCookieJar(jira.cookie)
            # manager.finished.connect(self.on_reply)
            # req = QtNetwork.QNetworkRequest(QtCore.QUrl(data['self']))
            # manager.get(req)

    def load_data_to_ui(self, data):
        fields = data['fields']
        print fields

        title = fields['summary']
        path = fields['project']['name'] + ' / ' + data['key']

        self.lbl_title.setText(title)
        self.setWindowTitle(path)

        type_str = u'类型：' + fields['issuetype']['name']
        pri_str = u'优先级：' + fields['priority']['name']
        status_str = u'状态：无'
        if fields['status'] != None:
            status_str = u'状态：' + fields['status']['name']
        reso_str = u'解决情况：无'
        if fields['resolution'] != None:
            reso_str = u'解决情况：' + fields['resolution']['name']
        version_str = u'修复版本：无'
        if len(fields['fixVersions']) > 0:
            version_str = u'修复版本：' + fields['fixVersions'][0]['name']

        components = u'模块：无'
        if len(fields['components']) > 0:
            components = u'模块：' + fields['components'][0]['name']

        assignee = u'经办人：' + fields['assignee']['displayName']
        reporter = u'报告人：' + fields['reporter']['displayName']
        votes = u'投票：' + str(fields['votes']['votes'])
        watches = u'关注：' + str(fields['watches']['watchCount'])

        created = u'创建：' + convert.utc_to_local(fields['created'])
        updated = u'更新：' + convert.utc_to_local(fields['updated'])

        self.lbl_detail1.setText(
            "<p style='line-height:20px'>" + type_str + '<br/>' + pri_str + '<br/>' + status_str + '<br/>' + reso_str + '</p>')
        self.lbl_detail2.setText(
            "<p style='line-height:20px'>" + components + '<br/>' + version_str + '<br/>' + assignee + '<br/>' + reporter + '</p>')
        self.lbl_detail3.setText(
            "<p style='line-height:20px'>" + created + '<br/>' + updated + '<br/>' + votes + '<br/>' + watches + '</p>')
        if fields['description'] != None:
            self.txt_desc.setPlainText(fields['description'])

        if len(fields['attachment']) > 0:
            for att in fields['attachment']:
                self.atts.append(att)
                btn = QPushButton()
                btn.setText(att['filename'])
                btn.setMaximumWidth(260)
                btn.setMinimumWidth(80)
                #事件绑定时传入参数
                self.connect(btn, SIGNAL("clicked()"), lambda arg=att: self.open_file_browser(arg))
                # lambda: self.open_file_browser(att))

                # btn.clicked.connect(self.open_web(att['content']))
                self.attachment_layout.addWidget(btn)

            lbl = QLabel()
            self.attachment_layout.addWidget(lbl)

    def open_file_browser(self, con):
        print con
        fileBrowser = file_browser.FileDialog(con, self.net_access)
        fileBrowser.setFixedSize(600, 500)
        fileBrowser.exec_()

    def net_access(self, api, reply_func):
        m1 = QtNetwork.QNetworkAccessManager(self)
        m1.setCookieJar(jira.cookie)
        m1.finished.connect(reply_func)
        req1 = QtNetwork.QNetworkRequest(QUrl(api))
        m1.get(req1)
        # try:
        # thum_file = att['thumbnail'].split('/')[-1]
        # label = QLabel()
        # png = QPixmap()
        # png.load("../../thumbnail/%s" % thum_file)
        # label.setPixmap(png)
        #     self.attachment_layout.addWidget(label)
        # except KeyError:
        #     btn = QPushButton()
        #     btn.setText(att['filename'])
        #     btn.setMaximumWidth(300)
        #     f = att['content'].split('/')[-1]
        #     self.connect(btn, SIGNAL("clicked()"), lambda: self.open_file_browser(f))
        #     # btn.clicked.connect(self.open_web(att['content']))
        #     self.attachment_layout.addWidget(btn)



        # self.web_attachment.load(QUrl('http://192.168.3.11:8080/secure/thumbnail/11556/_thumb_11556.png'))


        # self.web_attachment.load(QUrl('http://192.168.3.11:8080/secure/useravatar?avatarId=10122'))


        # def on_reply(self, reply):
        # if reply.error() != reply.NoError:
        # con = str(QString(reply.readAll()).toLatin1())
        #
        # try:
        # dicts = json.loads(con)
        # self.load_data_to_ui(dicts)
        # except ValueError:
        # pass
        # else:
        # # self.emit(SIGNAL("loginError"))
        # print 'load error'
        # print reply.error()
        # print reply.errorString()
