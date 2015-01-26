# coding=utf-8
__author__ = 'guguohai@outlook.com'

import cookielib
import urllib2
import json































class JIRA():
    def __init__(self, api_host):
        self.host = api_host
        cj = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cj)
        self.opener = urllib2.build_opener(handler)

        # cookie_txt = PATH('./FileCookieJar.txt')
        # self.fileCookieJar = cookielib.LWPCookieJar(cookie_txt)
        # self.fileCookieJar.save()
        # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.fileCookieJar))

        self.isActive = False
        self.starLogin = False
        self.displayName = ''
        self.userName = ''
        self.home_data = None
        self.project = None

    def login(self, u_name, u_pwd):
        url = '/rest/gadget/1.0/login?os_username=%s&os_password=%s&os_captcha=' % (u_name, u_pwd)
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

    def userActive(self, u_name):
        '''
        登录会405，用这个api获取用户是否活动状态
        :return:
        '''
        api_user = self.get('/rest/api/2/user?username=%s' % u_name)
        print api_user
        try:
            aa = api_user['errorMessages']
            self.isActive = False
        except KeyError:
            self.isActive = True
            self.displayName = api_user['displayName']
            self.userName = api_user['name']
            return api_user
        except TypeError:
            pass

    def get(self, api):
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