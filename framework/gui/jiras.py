# coding=utf-8
__author__ = 'guguohai@outlook.com'

import time
import threading
import cookielib
import urllib2
import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtNetwork
from framework.gui.ui import jira_main_ui
from framework.gui.models import jira_model
# import base
from framework.gui.base import *

JIRA_URL = 'http://192.168.3.11:8080'


class JIRAForm(QWidget, jira_main_ui.Ui_Form):
    def __init__(self,managers):
        super(JIRAForm, self).__init__()

        self.setupUi(self)
        self.table = None
        self.project = None
        self.tv_bugs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_bugs.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tv_bugs.setAlternatingRowColors(True)

        #self.connect(self, SIGNAL("issuesComplete"), self.setTableModel)
        #self.connect(self, SIGNAL("projectComplete"), self.setCmbProject)
        self.connect(self.btn_find, SIGNAL("clicked()"), self.findJiraData)

        # iss_url = '/rest/api/2/search?jql=project+%3D+' + project_name + '&startAt=' + start + '&maxResults=' + end
        p_name = 'IDRIVERC'
        start_page = 10

        end_page = start_page + meta.page_size
        iss_url = r'/rest/api/2/search?jql=project=' + p_name + '&startAt=' + str(start_page) + '&maxResults=' + str(
            end_page)  # % ('IDRIVERC', start_page, end_page)
        project_url = '/rest/api/2/project'
        self.host = 'http://192.168.3.11:8080'

        # self.netAccess(project_url, self.project_reply)
        # self.netAccess(iss_url, self.issues_reply)

        m1 = managers[0]
        m2 = managers[1]
        m1.setCookieJar(jira.cookie)
        m1.finished.connect(self.issues_reply)
        m1.get(self.qurl(iss_url))

        m2.setCookieJar(jira.cookie)
        m2.finished.connect(self.project_reply)
        m2.get(self.qurl(project_url))


    # def netAccess(self, api, reply_func):
    #     manager = QtNetwork.QNetworkAccessManager(self)
    #     manager.setCookieJar(jira.cookie)
    #     manager.finished.connect(reply_func)
    #
    #     req = QtNetwork.QNetworkRequest(QUrl(self.host + api))
    #     manager.get(req)


    def qurl(self, api):
        url = QUrl(JIRA_URL + api)
        return QtNetwork.QNetworkRequest(url)

    def project_reply(self, reply):
        if reply.error() == reply.NoError:
            con = unicode(QString(reply.readAll()))
            print 'project_reply::', con
            dicts = json.loads(con)
            for p in dicts:
                self.cmb_project.addItem(p['key'])


    def issues_reply(self, reply):
        if reply.error() == reply.NoError:
            con = unicode(QString(reply.readAll()))
            print 'issues_reply::', con
            dicts = json.loads(con)

            issues_data = []
            for issue in dicts['issues']:
                key = issue['key']
                summary = issue['fields']['summary']
                assignee = issue['fields']['assignee']['displayName']
                reporter = issue['fields']['reporter']['displayName']
                priority = issue['fields']['priority']['name']
                status = issue['fields']['status']['name']
                # iss_dict['resolution'] = issue['fields']['resolution']['name']
                created = issue['fields']['created']
                updated = issue['fields']['updated']
                iss_tup = (key, summary, assignee, reporter, priority, status, created, updated)
                issues_data.append(iss_tup)
            header = (u'编号', u'任务名称', u'任务状态', u'任务类型', u'优先级', u'执行人', u'创建人', u'创建时间')
            table_model = jira_model.MyTableModel(header, issues_data, self)
            self.tv_bugs.setModel(table_model)
            self.tv_bugs.setColumnWidth(0, 150)
            self.tv_bugs.setColumnWidth(1, 400)
        else:
            #print reply.error
            print reply.errorString()

    def setCmbProject(self, arg):
        for p in arg:
            self.cmb_project.addItem(p['key'])

    def findJiraData(self):
        pj = self.cmb_project.currentText()
        iss_url = '/rest/api/2/search?jql=project%%3D%s&startAt=%s&maxResults=%s' % (pj, '10', '20')
        # jira_data = LoadNetData(self, 'issuesComplete', iss_url)
        #jira_data.start()


# class LoadNetData(threading.Thread):
# def __init__(self, ui, sign_value, url):
#         threading.Thread.__init__(self)
#         self.thread_stop = False
#         self.ui = ui
#         self.url = url
#         self.sign_value = sign_value
#         self.result = None
#         self.isStart = False
#
#     def run(self):
#         while not self.thread_stop:
#             print 'thread:::', self.url
#             if not self.isStart:
#                 self.result = base.third.get(self.url)
#                 self.isStart = True
#
#             # 如果全部装载完成，则发信号
#             if self.result != None:
#                 if len(self.result) > 0:
#                     print 'finish~~~~'
#                     self.ui.emit(SIGNAL(self.sign_value), self.result)
#                     self.thread_stop = True
#             time.sleep(1)


