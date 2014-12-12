# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import subprocess
import threading
#from framework.core import the,device,task,idriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def main():
    pass
    # _task = task.Task(PATH('./testcase/'),2)
    # device_run = device.RunTest(_task)
    # device_run.start()

def run_ium(port):
    p1 = subprocess.Popen('appium --port %s' % port, stdout=subprocess.PIPE, shell=True)
    p1.stdout.read()

class MonitorOrder(threading.Thread):

    def __init__(self,port=4723):
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        p1 = subprocess.Popen('appium --port %s' % self.port, stdout=subprocess.PIPE, shell=True)
        p1.stdout.read()


def split211(file_path):
    f=open(file_path,'r')

    file_lines = 1700 #大文件行数
    num = 7 #人数

    every_line = int(file_lines / num) #每个人分配到的行数

    while file_lines > 0:
        temp = every_line

        new_file = open(PATH('./file%s.txt' % file_lines), 'w')
        while temp > 0:
            new_file.write(f.readline())
            temp = temp - 1

        file_lines = file_lines - every_line


if __name__ == "__main__":
    # #main()
    # import time
    # from framework.core import device
    #
    # dr = device.RunAppium(4725)
    # dr.start()
    # #
    # # p1 = subprocess.Popen('appium --port 4725',stdout=subprocess.PIPE,shell=True)
    # # os.popen('appium --port 4725')
    # #
    # # aa = p1.stdout.read()
    # # if 'debug: Non-default server args: {"port":4725}' in aa:
    #
    #
    # while 1:
    #     print 'gegwwwwww'
    #     time.sleep(2)

    # p1 = subprocess.Popen('appium --port %s' % 4723, stdout=subprocess.PIPE, shell=True)
    # p1.stdout.read()
    #
    # p2 = subprocess.Popen('appium --port %s' % 4726, stdout=subprocess.PIPE, shell=True)
    # p2.stdout.read()
    # from framework.core import the
    # ps = the.project_settings
    #
    # # mo = MonitorOrder(4723)
    # # mo.start()
    # # print 'fff'
    # aaa=[4723,4725]
    # for a in aaa:
    #     print a
    #     mo = MonitorOrder(a)
    #     mo.start()
    #     print mo.ident
    #     time.sleep(5)
    #
    # class DemoOne():
    #     def __init__(self,word):
    #         self.word = word
    #
    #     def do1(self):
    #         print self.word
    #
    #     def do2(self):
    #         return 'abcdddd'
    #
    # class DemoTwo():
    #     def __init__(self,inst=None):
    #         self.inst = inst('aad')
    #
    #     def dt1(self):
    #         return self.inst
    #
    # dt = DemoTwo(DemoOne)
    #
    # dt.dt1().do1()
    # print dt.dt1().do2()
    from framework.core import the
    def sql(self, sql, db_config='', size=0):

        from framework.util import mysql
        '''
        mysql数据查询，size大于0时为查询多条数据
        '''
        db_conf = 'database'
        if len(db_config.strip()) > 0:
            db_conf += ('_'+db_config)

        # url,usr,pwd,db_name,port
        DRIVER = 'idriver.android.driver'
        dbs = the.app_configs[DRIVER][db_conf].split('|')#  self.configs[db_conf].split('|')

        dbm = mysql.DBManager(dbs[0], dbs[1], dbs[2], dbs[3], int(dbs[4]))

        r = None

        cu = dbm.get_cursor()
        cu.execute(sql)
        if size == 0:
            r = cu.fetchone()
        elif size >= 1:
            r = cu.fetchall()
        else:
            print u'error'

        cu.close()
        dbm.close_db()
        return r

    split211(PATH('./k211_ddd.txt'))


    # for p in ps:
    #     port_ = 0
    #     try:
    #         remote_port = ps[p]['remote_port']
    #         port_ = int(remote_port)
    #     except KeyError:
    #         port_ = 0
    #
    #     if port_!=0:
    #         mo = MonitorOrder(port_)
    #         mo.start()