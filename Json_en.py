#-*-coding:utf-8 -*-
import json


def  parse_json():
    data = [{'a':'A','c':3.0,'b':(2,4)}] #list 对象
    print type(data)
    print "Data",repr(data)
    data_string = json.dumps(data)  # 将PYTHON对象转化成字符串
    print type(data_string)
    print data_string

def pare_json_object():
    data='{"name":"test","type":{"name":"seq","parameter":["1","2"]}}'
    s = json.loads(data)   #把字符串转化成Python 对象
    print s.keys()
    print s["name"]
    print s["type"]["name"]
    print s["type"]["parameter"][0]

if __name__ =="__main__":
    parse_json()
    pare_json_object()

