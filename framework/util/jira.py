# coding=utf-8
__author__ = 'Administrator'

import cookielib
import urllib
import urllib2
import json
import time
import threading


class JIRA():
    def __init__(self):
        self.host = 'http://192.168.3.11:8080'
        cj = cookielib.CookieJar()  # 获取cookiejar实例
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    def login(self, user, pwd):
        self.user = user
        self.pwd = pwd
        url = '/rest/gadget/1.0/login?os_username=%s&os_password=%s&os_captcha=' % (user, pwd)
        # data = {"os_username": username, "os_password": pwd}
        # urllib.urlencode(data)
        post_data = None
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
                   'Accept': 'application/json',
                   'Accept-Encoding': 'gzip, deflate',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Connection': 'keep-alive',
                   'Cache-Control': 'no-cache'
        }

        req = urllib2.Request(self.host+url, post_data, headers)

        try:
            self.opener.open(req, timeout=5)
        except urllib2.HTTPError:
            pass
            # print content.read()

        return self.userActive()


    def userActive(self):
        '''
        登录会405，用这个api获取用户是否活动状态
        :return:
        '''
        api_user = self.get('/rest/api/2/user?username=%s' % self.user)
        return api_user['active']


    def get(self, api):
        # url='http://192.168.3.11:8080/rest/api/2/user?username=%s' %self.user
        content = self.opener.open(self.host + api)

        try:
            return json.loads(content.read())
        except ValueError:
            return None

