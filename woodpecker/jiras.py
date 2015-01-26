# coding=utf-8
__author__ = 'guguohai@outlook.com'

import json
import os
from framework.core import box

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from woodpecker.views import jira_main_ui
from woodpecker.models import jira_model
from woodpecker.dialog import issue_detail, new_issue


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

ja = box.jira

jira_folder = PATH(ja.folder)


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
        self.connect(self.tv_bugs, SIGNAL("doubleClicked(const QModelIndex&)"), self.show_issue_detail)
        self.connect(self.cmb_pages, SIGNAL("activated(QString)"), self.onActivated)
        self.btn_prev.clicked.connect(self.prev_page)
        self.btn_next.clicked.connect(self.next_page)
        self.btn_new.clicked.connect(self.new_issue)
        # AND status=resolved
        # self.iss_url = r'/rest/api/2/search?jql=project=' + p_name + '&startAt=0&maxResults=' + str(jira.pageSize)
        # self.project_url = '/rest/api/2/project'

        self.btn_find.setText(u'查询中...')
        self.btn_find.setEnabled(False)
        self.lbl_results.setText('')
        self.cmb_project_current_txt = ja.default_project.upper()
        self.current_page = 0

        self.thumbs = []
        self.thumbs_index = 0
        # self.nam[0](self.iss_url, self.issues_reply)

        self.nam(ja.host + '/rest/api/2/project', self.project_reply)


    def get_issues(self, project_name, pages=0):
        self.iss_url = r'/rest/api/2/search?jql=project=' + project_name + '&startAt=' + str(
            pages) + '&maxResults=' + str(ja.pageSize)
        self.nam(ja.host + self.iss_url, self.issues_reply)

    def prev_page(self):
        pages = self.current_page - 1
        if pages >= 0:
            p = pages * ja.pageSize
            self.get_issues(self.cmb_project_current_txt, p)

            self.current_page = pages
            p_idx = self.cmb_pages.findText(str(pages + 1))
            self.cmb_pages.setCurrentIndex(p_idx)

    def next_page(self):
        pages = self.current_page + 1
        if self.cmb_pages.count() - 1 - pages >= 0:
            p = pages * ja.pageSize
            self.get_issues(self.cmb_project_current_txt, p)

            self.current_page = pages
            p_idx = self.cmb_pages.findText(str(pages + 1))
            self.cmb_pages.setCurrentIndex(p_idx)

    def new_issue(self):
        new_issue_dlg = new_issue.IssueDialog()
        new_issue_dlg.exec_()

    def show_issue_detail(self):
        idx = self.tv_bugs.currentIndex()
        if idx.isValid():
            self.currentRow = self.table_model.rowContent(idx.row())
            self.nam(self.currentRow['self'], self.issue_detail_reply)

    def issue_detail_reply(self, reply):
        if reply.error() == reply.NoError:
            con = str(QString(reply.readAll()).toLatin1())
            try:
                dicts = json.loads(con)
                # 下载附件
                # self.show_thumbnail(dicts['fields']['attachment'])
                self.issueDialog = issue_detail.IssueDialog(dicts)
                self.issueDialog.exec_()
            except ValueError:
                pass
        else:
            print reply.error()

    # def show_thumbnail(self, attachments):
    # self.thumbs = []
    #     self.thumbs_index = 0
    #     if len(attachments) > 0:
    #         for att in attachments:
    #             try:
    #                 th_url = att['thumbnail']
    #                 self.thumbs.append(th_url)
    #                 self.nam(th_url, self.issue_thumbnail_reply)
    #             except KeyError:
    #                 # 没有缩略图，就下载content 的url
    #                 th_url = att['content']
    #                 self.thumbs.append(th_url)
    #                 self.nam(th_url, self.issue_thumbnail_reply)
    #
    # def issue_thumbnail_reply(self, reply):
    #     if reply.error() == reply.NoError:
    #         # 从url中取文件名
    #         f_name = self.thumbs[self.thumbs_index].split('/')[-1]
    #         self._write_file(f_name, reply.readAll())
    #         self.thumbs_index += 1
    #     else:
    #         print 'thumbnail error!'

    def _write_file(self, filename, data):
        if os.path.exists(jira_folder):
            try:
                output_file = open(os.path.join(jira_folder, filename), 'wb')
                output_file.writelines(data)
                output_file.close()
                # print '文件 %s 写入完成！' % filename
            except IOError:
                print "写文件失败！"

    def onActivated(self, txt):
        self.current_page = int(txt) - 1
        self.get_issues(self.cmb_project_current_txt, self.current_page * ja.pageSize)

    def find_JIRA_Data(self):
        self.current_page = 0
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

            p_idx = self.cmb_project.findText(ja.default_project)
            self.cmb_project.setCurrentIndex(p_idx)
            # 等项目combobox加载完成后，再加载TableView
            self.get_issues(self.cmb_project_current_txt)


    def issues_reply(self, reply):
        if reply.error() == reply.NoError:
            all = reply.readAll()
            con = str(QString(all).toLatin1())
            print 'issues_reply::', con
            try:
                dicts = json.loads(con)
                issues = dicts['issues']

                # 索引为0，页数不能为0，所以余数+1的基础上再+1
                p = int(dicts['total'] / ja.pageSize) + 2

                # 如果是点击查询或首次加载，则重新载入页数
                if self.current_page == 0:
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


