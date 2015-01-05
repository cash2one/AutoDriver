# coding=utf-8
__author__ = 'guguohai@outlook.com'

import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.gui.ui import jira_main_ui
from framework.gui.models import jira_model
from framework.gui.base import *


class JIRAForm(QWidget, jira_main_ui.Ui_Form):
    def __init__(self, netAccess_method):
        super(JIRAForm, self).__init__()

        self.setupUi(self)
        self.nam = netAccess_method
        self.table = None
        self.project = None
        self.tv_bugs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_bugs.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tv_bugs.setAlternatingRowColors(True)
        self.tv_bugs.horizontalHeader().setStretchLastSection(True)

        self.connect(self.btn_find, SIGNAL("clicked()"), self.find_JIRA_Data)

        p_name = 'IDRIVERC'

        self.iss_url = r'/rest/api/2/search?jql=project=' + p_name + '&startAt=1&maxResults=' + str(jira.pagesize)
        self.project_url = '/rest/api/2/project'
        self.host = 'http://192.168.3.11:8080'

        self.btn_find.setText(u'查询中...')
        self.btn_find.setEnabled(False)
        self.lbl_results.setText('')

        self.nam[0](self.iss_url, self.issues_reply)
        self.nam[1](self.project_url, self.project_reply)


    def find_JIRA_Data(self):
        self.lbl_results.setText('')
        self.btn_find.setText(u'查询中...')
        self.btn_find.setEnabled(False)

        pj = self.cmb_project.currentText()
        iss_url = r'/rest/api/2/search?jql=project=' + pj + '&startAt=1&maxResults=' + str(jira.pagesize)
        self.nam[0](iss_url, self.issues_reply)

    def project_reply(self, reply):
        if reply.error() == reply.NoError:
            con = str(QString(reply.readAll()))
            print 'project_reply::', con
            dicts = json.loads(con)
            for p in dicts:
                self.cmb_project.addItem(p['key'])


    def issues_reply(self, reply):
        if reply.error() == reply.NoError:
            all = reply.readAll()
            print 'qqqq:::', all
            con = str(QString(all).toLatin1())
            print 'issues_reply::', con
            try:
                dicts = json.loads(con)
                issues = dicts['issues']

                p = int(dicts['total'] / jira.pagesize)

                self.cmb_pages.clear()
                for i in range(1, p):
                    self.cmb_pages.addItem(str(i))

                self.btn_find.setText(u'查询')
                self.btn_find.setEnabled(True)
                self.setJIRAModels(issues)
            except ValueError:
                self.btn_find.setText(u'查询')
                self.btn_find.setEnabled(True)
                self.lbl_results.setText(u'解析查询结果失败！')

        else:
            self.btn_find.setText(u'查询')
            self.btn_find.setEnabled(True)
            self.lbl_results.setText(u'查询失败！')
            print reply.errorString()


    def setJIRAModels(self, issues):
        issues_data = []
        for issue in issues:  # dicts['issues']:
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

        if len(issues_data) > 0:
            self.lbl_results.setText('')
            table_model = jira_model.MyTableModel(meta.task_header, issues_data, self)
            self.tv_bugs.setModel(table_model)
            # self.tv_bugs.setColumnWidth(0, 150)
            self.tv_bugs.setColumnWidth(1, 400)
            self.tv_bugs.setColumnWidth(2, 85)
            self.tv_bugs.setColumnWidth(3, 85)
            self.tv_bugs.setColumnWidth(4, 85)
            self.tv_bugs.setColumnWidth(5, 85)
        else:
            self.lbl_results.setText(u'没有任何数据！')
            self.tv_bugs.setModel(None)


