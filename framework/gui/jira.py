# coding=utf-8
__author__ = 'Administrator'

import time
import threading
import cookielib
import urllib2
import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.core import the
from framework.gui.ui import jira_main_ui, login_ui
from framework.gui.models import jira_model

JIRA_URL = 'http://192.168.3.11:8080'


class JIRAForm(QWidget, jira_main_ui.Ui_Form):
    def __init__(self):
        super(JIRAForm, self).__init__()

        self.setupUi(self)
        self.table = None
        self.project = None
        self.tv_bugs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_bugs.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tv_bugs.setAlternatingRowColors(True)

        self.connect(self, SIGNAL("issuesComplete"), self.setTableModel)
        self.connect(self, SIGNAL("projectComplete"), self.setCmbProject)
        self.connect(self.btn_find, SIGNAL("clicked()"), self.findJiraData)

        # iss_url = '/rest/api/2/search?jql=project+%3D+' + project_name + '&startAt=' + start + '&maxResults=' + end
        iss_url = '/rest/api/2/search?jql=project+%%3D+%s&startAt=%s&maxResults=%s' % ('IDRIVERC', '10', '20')
        project_url = '/rest/api/2/project'

        thread_issues = LoadNetData(self, 'issuesComplete', iss_url)
        thread_issues.start()

        thread_project = LoadNetData(self, 'projectComplete', project_url)
        thread_project.start()

    def setTableModel(self, arg):
        issues_data = []
        for issue in arg['issues']:
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
        header=(u'编号', u'任务名称', u'任务状态', u'任务类型', u'优先级', u'执行人', u'创建人', u'创建时间')
        tablemodel = jira_model.MyTableModel(header,issues_data, self)
        self.tv_bugs.setModel(tablemodel)
        self.tv_bugs.setColumnWidth(0, 150)
        self.tv_bugs.setColumnWidth(1, 400)

    def setCmbProject(self, arg):
        for p in arg:
            self.cmb_project.addItem(p['key'])

    def findJiraData(self):
        pj = self.cmb_project.currentText()
        iss_url = '/rest/api/2/search?jql=project%%3D%s&startAt=%s&maxResults=%s' % (pj, '10', '20')
        jira_data = LoadNetData(self, 'issuesComplete', iss_url)
        jira_data.start()


class LoadNetData(threading.Thread):
    def __init__(self, ui, sign_value, url):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.ui = ui
        self.url = url
        self.sign_value = sign_value
        self.result = None
        self.isStart = False

    def run(self):
        while not self.thread_stop:
            print 'thread:::', self.url
            if not self.isStart:
                self.result = the.JIRA.get(self.url)
                self.isStart = True

            # 如果全部装载完成，则发信号
            if self.result != None:
                if len(self.result) > 0:
                    print 'finish~~~~'
                    self.ui.emit(SIGNAL(self.sign_value), self.result)
                    self.thread_stop = True
            time.sleep(1)


class LoginDialog(QDialog, login_ui.Ui_Form):
    def __init__(self):
        super(LoginDialog, self).__init__()
        # QDialog.__init__(self)

        # self.ui = login_ja.Ui_Form()
        # self.ui.setupUi(self)
        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 10))
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.connect(self.btn_login, SIGNAL("clicked()"), self.login_action)
        self.connect(self.btn_cancel, SIGNAL("clicked()"), self.confirm)
        self.connect(self, SIGNAL("loginFinish"), self.confirm)
        self.connect(self, SIGNAL("loginError"), self.time_out)
        self.setBackgroundImg()


    def mousePressEvent(self, event):
        # 定义鼠标点击事件
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event):
        # 定义鼠标移动事件
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


    def setBackgroundImg(self):
        png = QPixmap(self)
        png.load("./ui/res/login.png")
        palette1 = QPalette(self)
        palette1.setBrush(self.backgroundRole(), QBrush(png))
        self.widget.setPalette(palette1)

    def time_out(self):
        self.lbl_info.setText(u'登录超时，账号密码错误.')

    def login_action(self):
        username = self.txt_username.text()
        pwd = self.txt_pwd.text()
        self.btn_login.setText(u'登录中..')
        self.btn_login.setEnabled(False)

        login = LoginFor405(self, username, pwd)
        login.start()

    def confirm(self):
        # self.ui.lineEditValidateNum.setText("XXXXXX")   #测试给弹出的对话框里的元素赋值
        self.reject()  # 关闭窗口


class LoginFor405(threading.Thread):
    '''
    JIRA405错误的解决方案
    '''

    def __init__(self, ui, u_name, u_pwd):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.isStartLogin = False
        self.ui = ui
        self.timeout = 15
        if the.JIRA == None:
            the.JIRA = JIRA(u_name, u_pwd)

    def run(self):
        while not self.thread_stop:
            if not the.JIRA.isActive:
                if not self.isStartLogin:
                    the.JIRA.login()
                    self.isStartLogin = True
                else:
                    the.JIRA.userActive()
                    self.timeout -= 1
            else:
                print 'login success!'
                # emit 方法用来发射信号
                self.ui.emit(SIGNAL("loginFinish"))
                self.stop()
            time.sleep(1)

            if self.timeout <= 0:
                self.ui.emit(SIGNAL("loginError"))
                self.stop()

    def stop(self):
        self.thread_stop = True


class JIRA():
    def __init__(self, u_name, u_pwd):
        self.host = JIRA_URL
        cj = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cj)
        self.opener = urllib2.build_opener(handler)

        # cookie_txt = PATH('./FileCookieJar.txt')
        # self.fileCookieJar = cookielib.LWPCookieJar(cookie_txt)
        # self.fileCookieJar.save()
        # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.fileCookieJar))

        self.isActive = False
        self.starLogin = False
        self.user = u_name
        self.pwd = u_pwd
        self.dislayName = ''
        self.userName=''
        self.home_data = None
        self.project = None
        self.page_size = 20

    def login(self):
        url = '/rest/gadget/1.0/login?os_username=%s&os_password=%s&os_captcha=' % (self.user, self.pwd)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
                   'Accept': 'application/json',
                   'Accept-Encoding': 'gzip, deflate',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Connection': 'keep-alive',
                   'Cache-Control': 'no-cache'
        }

        req = urllib2.Request(self.host + url, None, headers)

        try:
            self.opener.open(req)
        except urllib2.HTTPError:
            pass
        except urllib2.URLError, e:
            print e.message

    def userActive(self):
        '''
        登录会405，用这个api获取用户是否活动状态
        :return:
        '''
        api_user = self.get('/rest/api/2/user?username=%s' % self.user)
        print api_user
        try:
            aa = api_user['errorMessages']
            self.isActive = False
        except KeyError:
            self.isActive = True
            self.dislayName = api_user['displayName']
            self.userName = api_user['name']
            return api_user
        except TypeError:
            pass

    def get(self, api):
        # url='http://192.168.3.11:8080/rest/api/2/user?username=%s' %self.user
        json_str = ''
        try:
            content = self.opener.open(self.host + api)
            json_str = content.read()
        except urllib2.HTTPError:
            pass
        except urllib2.URLError, e:
            print e.message

        try:
            return json.loads(json_str)
        except ValueError:
            return None