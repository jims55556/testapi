# -*- coding:utf-8 -*-

import threading
from TestAllCass import *

def threads():
    threads=[]
    threads.append(threading.Thread(target=demo1))
    threads.append(threading.Thread(target=demo2))
    for th in threads:
        th.start()
    for th in threads:
        th.join()

threads()