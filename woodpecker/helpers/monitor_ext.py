# coding=utf-8
__author__ = 'Administrator'

import os
import time
import socket
import datetime
import threading
import httplib2
from framework.util import const, sinfo, sqlite


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
db_path = PATH('./db')
report_path = PATH('./report/')


def create_db(task_type):
    time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

    db = os.path.join(db_path, '%s.db' % time_str)
    dbm = sqlite.DBManager(db)

    sql_str = ''
    if task_type == const.TASK_SERVER:
        sql_str = 'create table if not exists info (' \
                  'id integer primary key,cpu varchar(50) NULL,memory varchar(50) NULL,' \
                  'lo_sent varchar(50) NULL,lo_recv varchar(50) NULL,eth0_sent varchar(50) NULL,eth0_recv varchar(50) NULL,' \
                  'update_time datetime NULL)'
    elif task_type == const.TASK_LOCAL:
        sql_str = 'create table if not exists info (' \
                  'id integer primary key,resp_time integer NULL,status integer NULL,' \
                  'update_time datetime NULL)'

    cu = dbm.get_cursor()
    cu.execute(sql_str)
    dbm.conn.commit()
    cu.close()
    return dbm


def isHostAddr(value):
    import re

    pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    match = pattern.match(value)
    if match:
        return True  # match.group()
    else:
        return False


def get_ip_address():
    tempSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tempSock.connect(('8.8.8.8', 80))
    addr = tempSock.getsockname()[0]
    tempSock.close()
    return addr


def writeHttpInfo(time_out, url, dbm):
    # url=readConfig('server', 'url')
    h = httplib2.Http(timeout=time_out)

    resp_tup = ()
    try:
        time_start = datetime.datetime.now()  # 记录发起请求初始时间

        headers_dict = {'cache-control': 'no-cache', 'Accept': 'application/json', 'charset': 'utf-8'}
        resp, content = h.request(url, "POST", headers=headers_dict)

        dur = datetime.datetime.now() - time_start
        resp_tup = (dur.microseconds / 1000, resp.status, datetime.datetime.now())
    except:
        resp_tup = (0, 0, 0)

    print resp_tup
    dbm.insert_value("INSERT INTO info values (NULL,?,?,?)", resp_tup)


class TaskThread(threading.Thread):
    def __init__(self, url, task_type):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.dbm = None
        self.url = url
        # self.mail_to = readConfig('server', 'mail')
        # create_folder()
        self.isStart = False
        self.task_type = task_type

    def run(self):
        while not self.thread_stop:

            if self.isStart:
                if self.dbm == None:
                    # 根据任务类型创建数据库
                    self.dbm = create_db(self.task_type)

                if self.task_type == const.TASK_LOCAL:
                    writeHttpInfo(100, self.url, self.dbm)
                elif self.task_type == const.TASK_SERVER:
                    try:
                        args = sinfo.poll(1)
                        sinfo.refresh_window(self.dbm, *args)
                    except (KeyboardInterrupt, SystemExit):
                        pass
            else:
                if self.dbm != None:
                    self.dbm.conn.close()
                    # 结束并发送邮件
                    # send_mail(self.mail_to,self.task_type)
                    self.dbm = None

            time.sleep(2)

    def start_exec(self):
        self.isStart = True

    def pause_exec(self):
        self.isStart = False

    def stop(self):
        self.thread_stop = True


class Socketer():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def server(self, task_thread):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)

        while True:
            connection, address = sock.accept()
            try:
                connection.settimeout(5)
                buff = connection.recv(1024)
                if const.MSG_START in buff:
                    task_thread.start_exec()
                    connection.send('monitor start...')
                elif const.MSG_STOP in buff:
                    task_thread.pause_exec()
                    connection.send('monitor stop...')
            except socket.timeout:
                print 'time out'
            connection.close()

    def client(self, cmd):
        # 客户端连接到监控服务器
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))

        time.sleep(2)
        sock.send(cmd)
        recv_remote = sock.recv(1024)
        sock.close()
        print recv_remote