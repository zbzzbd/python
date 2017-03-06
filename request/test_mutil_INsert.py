# -*- coding: utf-8 -*-
import  json
import  requests
import  unittest
import demjson

"""
批量插入多条请求API接口
"""
class  test_post_Mutil_Insert(unittest.TestCase):

    def setUp(self):
        self.url='http://resource.ggang.cn:8002/GGangResouces/AddResouces'
        self.url2='http://resource.ggang.cn:8002/GGangResouces/AddResoucesList'

        self.data=self.get_pram_data()
        self.appid="b2937442-45c1-45af-b3ca-9482834ae27e"
        json_data='{"data":'+str(self.data)+',"appid":"'+self.appid+'"}'

        #json_data='{"data":{"ProductName":"不锈钢板","Specification":"20.0*1500*6000","Material":"430","ProductType":"产品规格","Factory":"太钢","WareHouse":"新百发仓库(无锡)","WareHouseTel":"13262630280","Price":100,"Weight":100,"Province":"上海","City":"上海","Contact":"联系人","Tel":"13262630280","Number":"10","Piece":"10","SourceUrl":"http://www.tsgw.cc/","ProviderName":"泰山钢网"},"appid":"b2937442-45c1-45af-b3ca-9482834ae27e"}'
        #json_data1='{"data":[{"Province": "shanghai", "City": "shanghai", "SourceUrl": "http://www.tsgw.cc/", "Tel": "13262630280", "ProviderName": "ganggang", "Weight": 100, "Specification": "20.0*1500*6000", "Material": "430", "Factory": "ganggang", "ProductName": "houyaban", "WareHouseTel": "13262630280", "Contact": "lianxiren", "ProductType": "guige", "Number": "10", "WareHouse": "taicang", "Piece": 0, "Price": 100}], "appid": "b2937442-45c1-45af-b3ca-9482834ae27e"}'
        self.json_data=demjson.decode(json_data)
        print  self.json_data


    def test_Mutil(self):
        r = requests.post(self.url2,"",self.json_data)
        print r.status_code
        print r.content
        self.assertEqual(r.status_code,200)
        json_data= json.loads(str(r.content))
        print json_data["RetMsg"]
        print json_data["RetCode"]


    def get_pram_data(self):
        list=[]
        for i in range(0,2000):
            data={"ProductName":"houyaban","Specification":"20.0*1500*6000","Material":"430","ProductType":"guige","Factory":"ganggang","WareHouse":"taicang","WareHouseTel":"13262630280","Price":100,"Weight":100,"Province":"shanghai","City":"shanghai","Contact":"lianxiren","Tel":"13262630280","Number":"10","Piece":i,"SourceUrl":"http://www.tsgw.cc/","ProviderName":"ganggang"}
            list.append(data)
        list =demjson.encode(list)
        return list


    def tearDown(self):
        pass


