# coding=utf-8
__author__ = 'Administrator'

import os
import time
import threading
import psutil
import socket
import datetime
import httplib2
import constant

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


db_path = PATH('./db')
report_path = PATH('./report/')

def print_line(str):
    print str


def getCPUstate(interval=1):
    return str(psutil.cpu_percent(interval))
    #return (str(psutil.cpu_percent(interval)) + "%")

    #function of Get Memory
def getMemorystate():
    phymem = psutil.phymem_usage()
    buffers = getattr(psutil, 'phymem_buffers', lambda: 0)()
    cached = getattr(psutil, 'cached_phymem', lambda: 0)()
    used = phymem.total - (phymem.free + buffers + cached)
    # line = "%5s%% %6s/%s" % (
    #     phymem.percent,
    #     str(int(used / 1024 / 1024)) + "M",
    #     str(int(phymem.total / 1024 / 1024)) + "M"
    # )
    return str(int(used / 1024 / 1024))

def bytes2human(n):
    """
    >>> bytes2human(10000)
    '9.8 K'
    >>> bytes2human(100001221)
    '95.4 M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f %s' % (value, s)
    return '%.2f B' % (n)

def get_ip_address():
    tempSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tempSock.connect(('8.8.8.8', 80))
    addr = tempSock.getsockname()[0]
    tempSock.close()
    return addr

def poll(interval):
    """Retrieve raw stats within an interval window."""
    tot_before = psutil.network_io_counters()
    pnic_before = psutil.network_io_counters(pernic=True)
    # sleep some time
    time.sleep(interval)
    tot_after = psutil.network_io_counters()
    pnic_after = psutil.network_io_counters(pernic=True)
    # get cpu state
    cpu_state = getCPUstate(interval)
    # get memory
    memory_state = getMemorystate()
    return (tot_before, tot_after, pnic_before, pnic_after,cpu_state,memory_state)


def refresh_window(my_dbm,tot_before, tot_after, pnic_before, pnic_after,cpu_state,memory_state):
    info_sql = "INSERT INTO info values (NULL,?,?,?,?,?,?,?)"
    data = (cpu_state,memory_state,)

    nic_names = pnic_after.keys()
    nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)

    net_bytes = ()
    for name in nic_names:
        stats_before = pnic_before[name]
        stats_after = pnic_after[name]

        if name!='' and len(net_bytes)<3:
            bytes_sent = str(name)+'-sent:' + bytes2human(stats_after.bytes_sent - stats_before.bytes_sent) + '/s'
            bytes_recv = str(name)+'-recv:' + bytes2human(stats_after.bytes_recv - stats_before.bytes_recv) + '/s'

            net_bytes+=(bytes_sent,bytes_recv,)

    if len(net_bytes)<3:
        net_bytes+=('0','0')

    data+=net_bytes+(time.asctime(),)
    print data

    my_dbm.insert_value(info_sql,data)



def isHostAddr(value):
    import re
    pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    match = pattern.match(value)
    if match:
        return True  #match.group()
    else:
        return False


def create_db(task_type):
    import sqlite
    time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

    db = os.path.join(db_path, '%s.db' % time_str)
    dbm = sqlite.DBManager(db)

    sql_str = ''
    if task_type == constant.TASK_SERVER:
        sql_str = 'create table if not exists info (' \
                  'id integer primary key,cpu varchar(50) NULL,memory varchar(50) NULL,' \
                  'lo_sent varchar(50) NULL,lo_recv varchar(50) NULL,eth0_sent varchar(50) NULL,eth0_recv varchar(50) NULL,' \
                  'update_time datetime NULL)'
    elif task_type == constant.TASK_LOCAL:
        sql_str = 'create table if not exists info (' \
                  'id integer primary key,resp_time integer NULL,status integer NULL,' \
                  'update_time datetime NULL)'

    cu = dbm.get_cursor()
    cu.execute(sql_str)
    dbm.conn.commit()
    cu.close()
    return dbm

def writeHttpInfo(time_out,url,dbm):
    #url=readConfig('server', 'url')
    h=httplib2.Http(timeout=time_out)

    resp_tup=()
    try:
        time_start = datetime.datetime.now()#记录发起请求初始时间

        headers_dict={'cache-control':'no-cache','Accept': 'application/json','charset':'utf-8'}
        resp,content = h.request(url, "POST",headers=headers_dict)

        dur = datetime.datetime.now() - time_start
        resp_tup=(dur.microseconds/1000,resp.status,datetime.datetime.now())
    except:
        resp_tup = (0,0,0)

    print resp_tup
    dbm.insert_value("INSERT INTO info values (NULL,?,?,?)",resp_tup)


class TaskThread(threading.Thread):
    def __init__(self,url, task_type):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.dbm = None
        self.url=url
        #self.mail_to = readConfig('server', 'mail')
        #create_folder()
        self.isStart = False
        self.task_type = task_type

    def run(self):
        while not self.thread_stop:

            if self.isStart:
                if self.dbm == None:
                    #根据任务类型创建数据库
                    self.dbm = create_db(self.task_type)

                if self.task_type == constant.TASK_LOCAL:
                    writeHttpInfo(100,self.url,self.dbm)
                elif self.task_type == constant.TASK_SERVER:
                    try:
                        args = poll(1)
                        refresh_window(self.dbm, *args)
                    except (KeyboardInterrupt, SystemExit):
                        pass
            else:
                if self.dbm != None:
                    self.dbm.conn.close()
                    #结束并发送邮件
                    #send_mail(self.mail_to,self.task_type)
                    self.dbm = None

            time.sleep(2)

    def start_exec(self):
        self.isStart = True

    def pause_exec(self):
        self.isStart = False

    def stop(self):
        self.thread_stop = True