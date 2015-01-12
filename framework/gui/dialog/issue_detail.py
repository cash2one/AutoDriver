# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtNetwork

from framework.gui.views import issue_detail_ui,label_btn
from framework.util import convert
from framework.core import the
import file_browser


class IssueDialog(QDialog, issue_detail_ui.Ui_Dialog):
    def __init__(self, data=None):
        QDialog.__init__(self)

        self.data = data

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))

        self.txt_desc.setFrameShape(QFrame.NoFrame)
        self.lbl_att_title.hide()

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
            self.lbl_att_title.show()
            self.lbl_att_title.setContentsMargins(5,0,0,3)
            # scroll = QScrollArea()
            # scroll.setFrameShape(QFrame.NoFrame)
            # scroll.setMaximumWidth(16777215)
            # scroll.setContentsMargins(0, 0, 0, 0)
            # qvb_layout = QVBoxLayout()
            # qvb_layout.setMargin(0)
            # qvb_layout.setAlignment(Qt.AlignLeft)

            # scroll.setMaximumWidth(160)
            # scroll.setBackgroundRole(QPalette.BrightText)

            for att in fields['attachment']:
                # list_data.append(os.path.join(jira.folder, att['filename']))
                # self.atts.append(att)
                # btn = QPushButton()
                # btn.setMinimumHeight(25)
                #
                # btn.setStyleSheet(
                # "background-color:#ffffff;border:0;background-image:url(./views/res/add.png);background-repeat:no-repeat;padding:30px 0 0 0")
                # btn.setText(att['filename'])
                #
                # btn.setMaximumWidth(150)

                new_lbl = label_btn.LabelButton(self.desc_layout)
                new_lbl.setText("<a href='#'>" + att['filename'] + "</a>")
                new_lbl.setContentsMargins(5,0,0,3)
                new_lbl.setStyleSheet("background-color:#ffffff")
                # new_lbl.setStyleSheet("color:blue")
                new_lbl.setCursor(QCursor(Qt.PointingHandCursor))
                new_lbl.setFont(QFont("Microsoft YaHei", 9))
                #new_lbl.setWordWrap(True)


                # 事件绑定时传入参数
                if att.has_key('thumbnail'):
                    self.connect(new_lbl, SIGNAL("clicked()"),
                                 lambda con=att['content'], isPic=True: self.open_file_browser(con, isPic))
                else:
                    self.connect(new_lbl, SIGNAL("clicked()"),
                                 lambda con=att['content'], isPic=False: self.open_file_browser(con, isPic))
                #qvb_layout.addWidget(new_lbl)
                self.desc_layout.addWidget(new_lbl)


            # scroll.setWidget(qvb_layout)
            # widget = QWidget()
            # widget.setLayout(qvb_layout)
            # widget.setContentsMargins(0, 0, 0, 0)
            # scroll.setWidget(widget)


    def open_file_browser(self, con, isPic):
        print con, isPic
        fileBrowser = file_browser.FileDialog(con, isPic, self.net_access)
        #fileBrowser.setFixedSize(800, 600)
        fileBrowser.exec_()

    def net_access(self, api, reply_func):
        m1 = QtNetwork.QNetworkAccessManager(self)
        m1.setCookieJar(the.jira.cookie)
        m1.finished.connect(reply_func)
        req1 = QtNetwork.QNetworkRequest(QUrl(api))
        m1.get(req1)
        # try:
        # thum_file = att['thumbnail'].split('/')[-1]
        # label = QLabel()
        # png = QPixmap()
        # png.load("../../thumbnail/%s" % thum_file)
        # label.setPixmap(png)
        # self.attachment_layout.addWidget(label)
        # except KeyError:
        # btn = QPushButton()
        # btn.setText(att['filename'])
        # btn.setMaximumWidth(300)
        # f = att['content'].split('/')[-1]
        # self.connect(btn, SIGNAL("clicked()"), lambda: self.open_file_browser(f))
        # # btn.clicked.connect(self.open_web(att['content']))
        # self.attachment_layout.addWidget(btn)



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
