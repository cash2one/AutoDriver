# coding=utf-8
__author__ = 'Administrator'

import os
import cookielib
import urllib
import urllib2
import json
import time
import threading

JIRA_URL = 'https://hibernate.atlassian.net'#'http://192.168.3.11:8080'
#http://192.168.3.11:8080/rest/api/2/search?jql=project+%3D+{0}&startAt={1}&maxResults={2}

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
        self.dislayName= ''

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
        except urllib2.URLError,e:
            print e.message

    def userActive(self):
        '''
        登录会405，用这个api获取用户是否活动状态
        :return:
        '''
        api_user = self.get('/rest/api/2/user?username=%s' % self.user)

        try:
            aa = api_user['errorMessages']
            self.isActive = False
        except KeyError:
            self.isActive = True
            self.dislayName = api_user['displayName']
            return api_user
        except TypeError:
            pass


    def get(self, api):
        # url='http://192.168.3.11:8080/rest/api/2/user?username=%s' %self.user
        json_str=''
        try:
            content = self.opener.open(self.host + api)
            json_str = content.read()
        except urllib2.HTTPError:
            pass
        except urllib2.URLError,e:
            print e.message

        try:
            return json.loads(json_str)
        except ValueError:
            return None

    def caller(input, func):
        func(input)


