#-*- coding:utf-8 -*-
"""
json 深度解析

[{'a':1,'b':{1,2,3,4},'c':[1,2,3]}]
"""

def pasre_json(json_data):
    print json_data


if __name__ =='__main__':
    json_data=[{'a':1,'b':'{1,2,3,4}','c':[1,2,3]}]
    pasre_json(json_data)



