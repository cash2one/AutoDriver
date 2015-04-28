# coding=utf-8
__author__ = 'guohai@live.com'

import httplib2
import json
import time
import datetime
# import pycurl
import StringIO
import cookielib
import urllib
import urllib2
import strs


# def getWebContent(file_path, url):
# f = open(file_path, 'w')
# html = urllib2.urlopen(url).read()
# f.write(html)
# f.close()

def login(url, username, pwd):
    # http://192.168.3.11:8080/rest/gadget/1.0/login?os_username={0}&os_password={1}&os_captcha=
    data = {"os_username": username, "os_password": pwd}
    post_data = urllib.urlencode(data)
    cj = cookielib.CookieJar()  # 获取cookiejar实例
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # 自己设置User-Agent（可用于伪造获取，防止某些网站防ip注入）
    headers = {"User-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    website = url
    req = urllib2.Request(website, post_data, headers)
    content = opener.open(req)
    print content.read()


def getHttp(url):
    h = httplib2.Http(timeout=20)  # (".cache",timeout=20)
    return h.request(url, "POST",
                     headers={'cache-control': 'no-cache', "Accept": "application/json", 'charset': 'utf-8'})


def getReturnVal(url, interval=0.5):
    time.sleep(interval)
    h = httplib2.Http(".cache", timeout=20)
    resp, content = h.request(url, "POST",
                              headers={'cache-control': 'no-cache', "Accept": "application/json", 'charset': 'utf-8'})

    # csrf_val = content.split('csrf_token" value="')[1].split('">')[0]
    # print content.decode('utf-8'),url
    if resp.status == 200:
        # return json.loads(content)
        try:
            return json.loads(content)
        except ValueError:
            return content
    else:
        return None


def getHttpStatus(url, time_out):
    h = httplib2.Http(timeout=time_out)
    try:
        time_start = datetime.datetime.now()  # 记录发起请求初始时间

        headers_dict = {'cache-control': 'no-cache', 'Accept': 'application/json', 'charset': 'utf-8'}
        resp, content = h.request(url, "POST", headers=headers_dict)

        con_len = float(resp.get('content-length'))
        dur = datetime.datetime.now() - time_start

        resp_time = dur.seconds * 1000 * 1000 + dur.microseconds
        resp_time_ms = resp_time / float(1000)
        resp_time_sec = resp_time / float(1000 * 1000)

        resp_kbs = (con_len / 1024) / resp_time_sec
        resp_tup = (resp.status, resp_time_ms, resp_kbs)
        return resp_tup
    except:
        resp_tup = (408, 0, 0)
        return resp_tup


DEFAULT_OPTIONS = {
    "server": "http://localhost:2990/jira",
    "rest_path": "api",
    "rest_api_version": "2",
    "verify": True,
    "resilient": False,
    "async": False,
    "client_cert": None,
    "headers": {
        'X-Atlassian-Token': 'no-check',
        'Cache-Control': 'no-cache',
        #'Pragma': 'no-cache',
        #'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT'
    }
}

JIRA_BASE_URL = '{server}/rest/api/{rest_api_version}/{path}'

def _get_url(self, path, base=JIRA_BASE_URL):
    options = self._options
    options.update({'path': path})
    return base.format(**options)

class TestJIRA():
    def __init__(self):
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.host = 'http://192.168.3.11:8080'
        self.user_name = 'guguohai'
        self.pwd = 'guguohai'

    def login(self):
        url = '/rest/gadget/1.0/login?os_username=%s&os_password=%s&os_captcha=' % (self.user_name, self.pwd)
        req = urllib2.Request(self.host + url)
        req.add_header('Content-type', 'application/json')
        data = None

        try:
            response = self.opener.open(req, data)
            print response.read()
        except urllib2.HTTPError:
            pass
            # print response.read()

    def get_user(self):
        url = '/rest/api/2/user?username=%s' % self.user_name
        req = urllib2.Request(self.host + url)
        req.add_header('Content-type', 'application/json')
        data = None

        try:
            response = self.opener.open(req, data)
            print response.read()
        except urllib2.HTTPError:
            pass

    def createmeta(self):
        url = '/rest/api/2/issue/createmeta?projectIds=10303&projectKeys=CI-64&issuetypeIds=3&issuetypeNames=任务'
        req = urllib2.Request(self.host + url)
        req.add_header('Content-type', 'application/json')
        data = None

        try:
            response = self.opener.open(req, data)
            print response.read()
        except urllib2.HTTPError:
            pass

    def create_issue(self):#, fields=None, prefetch=True, **fieldargs):
        #
        # data = {}
        # if fields is not None:
        #     data['fields'] = fields
        # else:
        #     fields_dict = {}
        #     for field in fieldargs:
        #         fields_dict[field] = fieldargs[field]
        #     data['fields'] = fields_dict
        #

        #r = self._session.post(url, headers={'content-type': 'application/json'}, data=json.dumps(data))
        url = '/rest/api/2/issue'#/createmeta?projectIds=10303&projectKeys=CI-64&issuetypeIds=3&issuetypeNames=任务'
        req = urllib2.Request(self.host + url)
        req.add_header('Content-type', 'application/json')
        # headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        # 'Content-type': 'application/json'}

        # data_dict = {
        #     'fields': {
        #         'project': {
        #             'id': '10303'
        #         },
        #         'summary': 'something s wrongfff',
        #         'issuetype': {
        #             'id': '3'
        #         },
        #         'assignee': {
        #             'name': 'guguohai'
        #         },
        #         'reporter': {
        #             'name': 'guguohai'
        #         },
        #         'priority': {
        #             'id': '20000'
        #         },
        #         'labels': [],
        #         'timetracking': {
        #             'originalEstimate': '10',
        #             'remainingEstimate': '5'
        #         },
        #         'versions': [
        #             {
        #                 'id': '10364'
        #             }
        #         ],
        #         'environment': 'environment',
        #         'description': 'description',
        #         'duedate': '2011-03-11',
        #         'fixVersions': [
        #             {
        #                 'id': '10364'
        #             }
        #         ]
        #     }
        # }

        ddd={
            "fields": {
               "project":
               {
                  "key": "CI"
               },
               "summary": "REST ye merry gentlemen.",
               "description": "Creating of an issue using project keys and issue type names using the REST API",
               "issuetype": {
                  "name": "Bug"
               }
           }
        }
        data = urllib.urlencode(ddd)


        try:
            response = self.opener.open(req, data)
            print response.read()
        except urllib2.HTTPError, e:
            print 'eeeeeee', e.code
