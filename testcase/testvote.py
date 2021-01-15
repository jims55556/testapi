# -*- coding:utf-8 -*-
import xlrd
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath



testdata=xlrd.open_workbook(GetTestDataPath())



testurl="http://127.0.0.1:8000"
def post_vote():
    try:
        table = testdata.sheets()[0]
        for i in range(3,5):
            choice=table.cell(i,0).value
            status=table.cell(i,1).value
            qiwang = table.cell(i, 2).value
            hdata={
                'choice':int(choice)
            }
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid="1-1"
            testname="testvote"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestPostRequest(testurl+'/poll/1/vote/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe)
    except Exception as e:
        print(e)
# post_vote()

def get_polls():
    try:
        table = testdata.sheets()[0]
        for i in range(13,14):
            status = table.cell(i, 0).value
            qiwang = table.cell(i, 1).value
            hdata=""
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid="1-1"
            testname="testpolls"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/poll/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status")
    except Exception as e:
        print(e)

# get_polls()
