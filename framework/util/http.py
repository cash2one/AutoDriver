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


# def getWebContent(file_path, url):
#     f = open(file_path, 'w')
#     html = urllib2.urlopen(url).read()
#     f.write(html)
#     f.close()

def login(url, username, pwd):
    #http://192.168.3.11:8080/rest/gadget/1.0/login?os_username={0}&os_password={1}&os_captcha=
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
    h = httplib2.Http(timeout=20)  #(".cache",timeout=20)
    return h.request(url, "POST",
                     headers={'cache-control': 'no-cache', "Accept": "application/json", 'charset': 'utf-8'})


def getReturnVal(url, interval=0.5):
    time.sleep(interval)
    h = httplib2.Http(".cache", timeout=20)
    resp, content = h.request(url, "POST",
                              headers={'cache-control': 'no-cache', "Accept": "application/json", 'charset': 'utf-8'})

    #csrf_val = content.split('csrf_token" value="')[1].split('">')[0]
    #print content.decode('utf-8'),url
    if resp.status == 200:
        #return json.loads(content)
        try:
            return json.loads(content)
        except ValueError:
            return content
    else:
        return None


def getHttpStatus(url, time_out):
    h = httplib2.Http(timeout=time_out)
    try:
        time_start = datetime.datetime.now()  #记录发起请求初始时间

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


# def getcurl(input_url,timeout):
#
#     c = pycurl.Curl()
#
#     b = StringIO.StringIO()
#
#     c.setopt(pycurl.URL,input_url)
#     c.setopt(pycurl.HTTPHEADER, ["cache-control:no-cache,Accept:application/json,charset:utf-8"])
#
#     c.setopt(pycurl.WRITEFUNCTION, b.write)
#     c.setopt(pycurl.FOLLOWLOCATION, 1)
#     c.setopt(pycurl.HEADER, True)
#     c.setopt(pycurl.CONNECTTIMEOUT,timeout)
#     c.setopt(pycurl.TIMEOUT,timeout)
#     c.setopt(pycurl.USERAGENT,'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0')
#
#     c.perform()
#
#     #print b.getvalue()
#     #print c.getinfo(pycurl.TOTAL_TIME)
#
#
#     b.close()
#     c.close()

