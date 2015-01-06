# coding=utf-8
__author__ = 'guguohai@outlook.com'

import json
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.ui import issue_detail_ui
from framework.util import convert
from framework.gui.base import *


class IssueDialog(QDialog, issue_detail_ui.Ui_Dialog):
    def __init__(self, data=None):
        QDialog.__init__(self)

        self.data = data

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
        self.lbl_title.setWordWrap(True)
        self.web_attachment.hide()

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

        title = fields['summary']
        path = fields['project']['name'] + ' / ' + data['key']

        self.lbl_title.setText(title)
        self.setWindowTitle(path)

        type_str = u'类型：' + fields['issuetype']['name']
        pri_str = u'优先级：' + fields['priority']['name']
        status_str = u'状态：' + fields['status']['name']
        reso_str = u'解决情况：' + fields['resolution']['name']
        version_str = u'修复版本：无'
        if fields['fixVersions'] != None:
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

        self.lbl_detail1.setText(type_str + '\r\n' + pri_str + '\r\n' + status_str + '\r\n' + reso_str)
        self.lbl_detail2.setText(components + '\r\n' + version_str + '\r\n' + assignee + '\r\n' + reporter)
        self.lbl_detail3.setText(created + '\r\n' + updated + '\r\n' + votes + '\r\n' + watches)

        self.txt_desc.setPlainText(fields['description'])

        if len(fields['attachment']) > 0:
            self.web_attachment.show()
            # self.web_attachment.load(QUrl('http://192.168.3.11:8080/secure/thumbnail/11556/_thumb_11556.png'))



            # self.web_attachment.load(QUrl('http://192.168.3.11:8080/secure/useravatar?avatarId=10122'))


            # def on_reply(self, reply):
            # if reply.error() != reply.NoError:
            # con = str(QString(reply.readAll()).toLatin1())
            #
            #         try:
            #             dicts = json.loads(con)
            #             self.load_data_to_ui(dicts)
            #         except ValueError:
            #             pass
            #     else:
            #         # self.emit(SIGNAL("loginError"))
            #         print 'load error'
            #         print reply.error()
            #         print reply.errorString()
