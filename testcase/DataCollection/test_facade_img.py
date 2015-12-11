# coding=utf-8
__author__ = 'gghsean@163.com'

import os
import time
import re
import urllib2
import xlwt
from drivers import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.is_down_small = False


    def tearDown(self):
        self.driver.close()

    def test_cadillac(self):
        hrefs = []
        small_imgs = []
        car_alls = self.driver.find_id('all').find_classes('car_all')
        for car_all in car_alls:
            links = car_all.find_tags('a')
            imgs = car_all.find_tags('img')
            for img in imgs:
                small_imgs.append(img.get_attribute('src'))

            for a in links:
                hrefs.append(a.get_attribute('href'))

        print small_imgs
        print hrefs

        for img_url in small_imgs:
            self.download_img(img_url)

        for href in hrefs:
            print href, '----'
            time.sleep(1)
            self.download_img_from_html(href)


    def download_img_from_html(self, url):
        req = urllib2.Request(url)
        req.add_header('Content-type', 'text/html')
        data = None

        try:
            response = self.opener.open(req, data)
            html = response.read()
            start = html.find('server-date="')

            sd = re.compile(r'(?<=server-date=\").*?(?=\")')
            img_urls = sd.findall(html)

            if len(img_urls) <= 0:
                ds = re.compile(r'(?<=date-src=\").*?(?=\")')
                img_urls = ds.findall(html)

            for u in img_urls:
                self.download_img(u)

        except urllib2.HTTPError:
            pass

    def download_img(self, url):
        # 根据url建立文件夹和文件
        url_array = url.split('/')
        file_name = url_array[-1]
        folder = url_array[-2]

        req = urllib2.Request(url)
        req.add_header('Content-type', 'image/jpeg')
        data = None
        time.sleep(0.5)
        try:
            response = self.opener.open(req, data)
            img_folder = PATH('../../temporary/%s' % folder)

            if not os.path.exists(img_folder):
                os.mkdir(img_folder)

            f = open(os.path.join(img_folder, file_name), 'wb')
            f.write(response.read())
            f.close()
            print 'img_finish---'

        except urllib2.HTTPError:
            pass
