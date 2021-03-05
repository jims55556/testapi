# -*- coding:utf-8 -*-

import json
import requests
from log import logger
hlist=[]

header = {
'content-type': "application/json;charset=UTF-8"
}
# header = {
# 'content-type': "application/x-www-form-urlencoded"
# }

def TestPostRequest(hurl,hdata,headers,htestcassid,htestcasename,htesthope,fanhuitesthope):
    hr = requests.post(hurl, data=hdata, headers=headers)
    # hr=requests.post(hurl,data=json.dumps(hdata),headers=header)
    hresult=json.loads(hr.text)
    hstatus=hresult['status']
    if hstatus==htesthope and fanhuitesthope in str(hresult):
        hhhdata={"t_id":htestcassid,
                 "t_name":htestcasename,
                 "t_method":"POST",
                "t_url":hurl,
                 "t_param":"测试数据:"+str(hdata),
                 "t_hope":"status:"+htesthope+"期望结果："+fanhuitesthope,
                 "t_actual":"status:"+hstatus+"实际返回结果："+str(hresult),
                 "t_result":"通过"
        }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("通过")
        logger.info("实际返回结果："+str(hresult))
    else:
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcasename,
                   "t_method": "POST",
                   "t_url": hurl,
                   "t_param": "测试数据:" + str(hdata),
                   "t_hope": "status:" + htesthope + "期望结果：" + fanhuitesthope,
                   "t_actual": "status:" + hstatus + "实际返回结果：" + str(hresult),
                   "t_result": "失败"
                   }
        hlist.append(hhhdata)
        logger.error(htestcasename)
        logger.error("失败")
        logger.error("实际返回结果：" + str(hresult))
    print(hlist)


def TestGetRequest(hurl,hdata,headers,htestcassid,htestcasename,htesthope,fanhuitesthope,st):
    if hdata=="":
        hr = requests.get(hurl,headers=headers)
    else:
        hr = requests.get(hurl, params=hdata)
    hresult=json.loads(hr.text)
    hstatus=str(hresult[st])
    if hstatus==htesthope and fanhuitesthope in str(hresult):
        hhhdata={"t_id":htestcassid,
                 "t_name":htestcasename,
                 "t_method":"GET",
                "t_url":hurl,
                 "t_param":"测试数据:"+str(hdata),
                 "t_hope":"status:"+htesthope+"期望结果："+fanhuitesthope,
                 "t_actual":"status:"+hstatus+"实际返回结果："+str(hresult),
                 "t_result":"通过"
        }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("通过")
        logger.info("实际返回结果：" + str(hresult))
    else:
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcasename,
                   "t_method": "GET",
                   "t_url": hurl,
                   "t_param": "测试数据:" + str(hdata),
                   "t_hope": "status:" + htesthope + "期望结果：" + fanhuitesthope,
                   "t_actual": "status:" + hstatus + "实际返回结果：" + str(hresult),
                   "t_result": "失败"
                   }
        hlist.append(hhhdata)
        logger.error(htestcasename)
        logger.error("失败")
        logger.error("实际返回结果：" + str(hresult))
    print(hlist)

def TestDeleteRequest(hurl,hdata,headers,htestcassid,htestcasename,htesthope,fanhuitesthope):
    hr = requests.delete(hurl, data=hdata, headers=headers)#这个是删除请求使用的方法
    # hr=requests.post(hurl,data=json.dumps(hdata),headers=header)#同post请求的解释相一致
    hresult=json.loads(hr.text)
    hstatus=hresult['status']
    if hstatus==htesthope and fanhuitesthope in str(hresult):
        hhhdata={"t_id":htestcassid,
                 "t_name":htestcasename,
                 "t_method":"POST",
                "t_url":hurl,
                 "t_param":"测试数据:"+str(hdata),
                 "t_hope":"status:"+htesthope+"期望结果："+fanhuitesthope,
                 "t_actual":"status:"+hstatus+"实际返回结果："+str(hresult),
                 "t_result":"通过"
        }
        hlist.append(hhhdata)
    else:
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcasename,
                   "t_method": "POST",
                   "t_url": hurl,
                   "t_param": "测试数据:" + str(hdata),
                   "t_hope": "status:" + htesthope + "期望结果：" + fanhuitesthope,
                   "t_actual": "status:" + hstatus + "实际返回结果：" + str(hresult),
                   "t_result": "失败"
                   }
        hlist.append(hhhdata)
    print(hlist)



