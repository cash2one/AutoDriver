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


def print_line(str):
    print str


def getCPUstate(interval=1):
    return str(psutil.cpu_percent(interval))
    # return (str(psutil.cpu_percent(interval)) + "%")

    #function of Get Memory


def getMemorystate():
    phymem = psutil.phymem_usage()
    buffers = getattr(psutil, 'phymem_buffers', lambda: 0)()
    cached = getattr(psutil, 'cached_phymem', lambda: 0)()
    used = phymem.total - (phymem.free + buffers + cached)
    # line = "%5s%% %6s/%s" % (
    # phymem.percent,
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
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f %s' % (value, s)
    return '%.2f B' % (n)


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
    return (tot_before, tot_after, pnic_before, pnic_after, cpu_state, memory_state)


def refresh_window(my_dbm, tot_before, tot_after, pnic_before, pnic_after, cpu_state, memory_state):
    info_sql = "INSERT INTO info values (NULL,?,?,?,?,?,?,?)"
    data = (cpu_state, memory_state,)

    nic_names = pnic_after.keys()
    nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)

    net_bytes = ()
    for name in nic_names:
        stats_before = pnic_before[name]
        stats_after = pnic_after[name]

        if name != '' and len(net_bytes) < 3:
            bytes_sent = str(name) + '-sent:' + bytes2human(stats_after.bytes_sent - stats_before.bytes_sent) + '/s'
            bytes_recv = str(name) + '-recv:' + bytes2human(stats_after.bytes_recv - stats_before.bytes_recv) + '/s'

            net_bytes += (bytes_sent, bytes_recv,)

    if len(net_bytes) < 3:
        net_bytes += ('0', '0')

    data += net_bytes + (time.asctime(),)
    print data

    my_dbm.insert_value(info_sql, data)



