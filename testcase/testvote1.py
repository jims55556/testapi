# -*- coding:utf-8 -*-
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
#上面2行代码是将刚才所讲的TestRequest模块中的post和get请求方法导入进来使用

testurl="http://127.0.0.1:8000" #定义接口的主请求地址(ip+端口）
def post_vote(): #这个是测试投票接口的测试用例
    try:

            choice=1    #选定问题id为1的id为1的选项
            status='200' #这个是校验使用的逾期结果
            qiwang = 'success' #同上
            hdata={
                'choice':int(choice)
            }
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid="1-1" #设置测试用例的编号为"1-1"
            testname="testvote"+testcaseid#测试用例名称是写成固定的格式的
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestPostRequest(testurl+'/poll/1/vote/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe)
    except Exception as e: #这里使用的异常的处理方式，如果有异常然后按照下面的逻辑处理
           print(e)
post_vote()

def get_polls(): #这个测试查询所有问题接口用例
    try:
            status = '200'
            qiwang = 'success'
            hdata=""  #这个因为不需要传入参数，所以设置为空
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid="1-1"
            testname="testpolls"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/poll/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe)
            #r=TestGetRequest(testurl+'/poll/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status")
    except Exception as e:
        print(e)
# get_polls()