# -*- coding:utf-8 -*-

import  threading
import  time

stime=time.time()

def demo1(m):
    for i in range(1000):
        print(i+m)
    time.sleep(2)

def demo2(m):
    for i in range(2000):
        print(i+m)
    time.sleep(2)

def demo3(m):
    for i in range(500):
        print(i+m)
    time.sleep(2)



t1=threading.Thread(target=demo1,args=(1,))
t2=threading.Thread(target=demo2,args=(2,))
t3=threading.Thread(target=demo3,args=(3,))


threads=[]
threads.append(t1)
threads.append(t2)
threads.append(t3)
for th in threads:
    th.start()

for th in threads:
    th.join()


etime=time.time()

print(etime-stime)