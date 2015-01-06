# coding=utf-8
__author__ = 'guguohai@outlook.com'

import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.gui.ui import jira_main_ui, issue_detail_ui
from framework.gui.models import jira_model
from framework.gui.base import *
import issue_detail


class JIRAForm(QWidget, jira_main_ui.Ui_Form):
    def __init__(self, netAccess_method):
        super(JIRAForm, self).__init__()

        self.setupUi(self)
        self.nam = netAccess_method
        self.table_model = None

        self.project = None
        self.tv_bugs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_bugs.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tv_bugs.setAlternatingRowColors(True)

        self.currentRow = None

        self.connect(self.btn_find, SIGNAL("clicked()"), self.find_JIRA_Data)
        self.connect(self.tv_bugs, SIGNAL("doubleClicked(const QModelIndex&)"), self.show_issue)
        self.connect(self.cmb_pages, SIGNAL("activated(QString)"), self.onActivated)
        # AND status=resolved
        # self.iss_url = r'/rest/api/2/search?jql=project=' + p_name + '&startAt=0&maxResults=' + str(jira.pageSize)
        # self.project_url = '/rest/api/2/project'

        self.btn_find.setText(u'查询中...')
        self.btn_find.setEnabled(False)
        self.lbl_results.setText('')
        self.cmb_project_current_txt = 'IDRIVER'
        self.cmb_project_index = ''
        # self.nam[0](self.iss_url, self.issues_reply)
        self.get_issues(self.cmb_project_current_txt)
        self.nam[1](jira.host + '/rest/api/2/project', self.project_reply)


    def get_issues(self, project_name, pages=0):
        self.iss_url = r'/rest/api/2/search?jql=project=' + project_name + '&startAt=' + str(
            pages) + '&maxResults=' + str(jira.pageSize)
        self.nam[0](jira.host + self.iss_url, self.issues_reply)

    def show_issue(self):
        idx = self.tv_bugs.currentIndex()
        if idx.isValid():
            self.currentRow = self.table_model.rowContent(idx.row())
            self.nam[0](self.currentRow['self'], self.load_issue_reply)

    def load_issue_reply(self, reply):
        if reply.error() == reply.NoError:
            con = str(QString(reply.readAll()).toLatin1())
            try:
                dicts = json.loads(con)
                self.issueDialog = issue_detail.IssueDialog(dicts)
                self.issueDialog.exec_()
            except ValueError:
                pass
        else:
            # self.emit(SIGNAL("loginError"))
            print 'load error'
            print reply.error()
            print reply.errorString()
            # self.dlgTask.btn_ok.clicked.connect(self.save_current_task)

    def onActivated(self, txt):
        self.cmb_project_index = txt
        # type_idx = self.cmb_TaskType.findText(self.data[2])
        # self.cmb_TaskType.setCurrentIndex(type_idx)

        self.get_issues(self.cmb_project_current_txt, int(txt) * jira.pageSize)
        # self.label.setText(txt)
        # self.label.adjustSize()

    def find_JIRA_Data(self):
        self.cmb_project_index = ''
        self.lbl_results.setText('')
        self.btn_find.setText(u'查询中...')
        self.btn_find.setEnabled(False)
        self.cmb_project_current_txt = self.cmb_project.currentText()
        self.get_issues(self.cmb_project.currentText())

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

                p = int(dicts['total'] / jira.pageSize)

                # 如果是点击查询或首次加载，则重新载入页数
                if len(str(self.cmb_project_index).strip()) == 0:
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
        if len(issues) > 0:
            self.lbl_results.setText('')
            self.table_model = jira_model.MyTableModel(issues, self)
            self.tv_bugs.setModel(self.table_model)
            self.tv_bugs.setColumnWidth(0, 120)
            self.tv_bugs.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
            self.tv_bugs.setColumnWidth(7, 140)
            self.tv_bugs.setColumnWidth(8, 140)
            # self.tv_bugs.resizeColumnToContents(7)#自适应内容宽度

        else:
            self.lbl_results.setText(u'没有任何数据！')
            self.tv_bugs.setModel(None)


