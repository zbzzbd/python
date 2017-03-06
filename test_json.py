#-*- coding:utf-8 -*-
import  demjson

def Pare_json():
    data='{"data":[{},{}],"appid":"1234"}'
    data=[{'Province': 'shanghai', 'City': 'shanghai', 'SourceUrl': 'http://www.tsgw.cc/', 'Tel': '13262630280', 'ProviderName': 'ganggang', 'Weight': 100, 'Specification': '20.0*1500*6000', 'Material': '430', 'Factory': 'ganggang', 'ProductName': 'houyaban', 'WareHouseTel': '13262630280', 'Contact': 'lianxiren', 'ProductType': 'guige', 'Number': '10', 'WareHouse': 'taicang', 'Piece': 0, 'Price': 100}]

    json_data=demjson.encode(data)
    print json_data


if __name__=="__main__":
    Pare_json()