#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
def GetTestDataPath():
    ospath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath,"testdata","TestData.xls")

def GetTestReport():
    now = time.strftime("%Y-%m-%d-%H-%M-%S-", time.localtime(time.time()))
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "testreport", now +"TestReport.xls")

def GetTestLogPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "logs", "log.txt")


def GetTestConfig(configname):
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", configname)


# print(GetTestDataPath())

# print(GetTestLogPath())

# print(GetTestConfig('logconfig.conf'))