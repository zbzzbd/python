# -*- coding: utf-8 -*-
import  json
import  requests
import  unittest
import  HttpLibrary
import  RequestsLibrary

class Test_Robot_post(unittest.TestCase):



    def setUp(self):
        self.url = 'http://resource.ggang.cn:8002/GGangResouces/AddResouces'
        self.data = '{"ProductName":"不锈钢板","Specification":"20.0*1500*6000","Material":"430","ProductType":"产品规格","Factory":"太钢","WareHouse":"新百发仓库(无锡)","WareHouseTel":"13262630280","Price":100,"Weight":100,"Province":"上海","City":"上海","Contact":"联系人","Tel":"13262630280","Number":"10","Piece":"10","SourceUrl":"http://www.tsgw.cc/","ProviderName":"泰山钢网"}'
        # self.data=self.get_pram_data()
        self.appid = "b2937442-45c1-45af-b3ca-9482834ae27e"
        json_data = {"data":' + self.data + ',"appid":"' + self.appid + '"}
        # json_data='{"data":'+self.data+'}'
        # json_data='{"data":{"ProductName":"不锈钢板","Specification":"20.0*1500*6000","Material":"430","ProductType":"产品规格","Factory":"太钢","WareHouse":"新百发仓库(无锡)","WareHouseTel":"13262630280","Price":100,"Weight":100,"Province":"上海","City":"上海","Contact":"联系人","Tel":"13262630280","Number":"10","Piece":"10","SourceUrl":"http://www.tsgw.cc/","ProviderName":"泰山钢网"},"appid":"b2937442-45c1-45af-b3ca-9482834ae27e"}'
        self.json_data = json_data
        print  self.json_data

    def Test_Mutil(self):
        RequestsLibrary.RequestsKeywords.create_session('api',self.url,{})



    def tearDown(self):
        pass