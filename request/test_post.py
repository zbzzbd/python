import  unittest
import  json
import requests
from requests.auth import  HTTPBasicAuth

class jenins_test_get(unittest.TestCase):

    def setUp(self):
        self.r = requests.get('http://web.1xinxi.cn/asmx/smsservice.aspx?name=13818727639&pwd=EA4D4F2D1884447F541B47EE448B&content=aaa&mobile=13611873856&type=pt')
        print "start"

    def test_get_code(self):
       # result=self.r.text
        #json_result = json.loads(result)
        #self.assertEqual(json_result["jobs"][0]["name"],"test_ganggang_ui")
        #self.assertEqual(json_result["jobs"][-1]["name"],"test_ggang_demo")
        #print json_result["jobs"]
        result=self.r.content
        print type(result)
        print self.r.status_code
        print self.r.content

    def test_get_all_job_names_simple(self):
        #json_result = self.r.json()
        #self.assertEqual(json_result["jobs"][0]["name"], "test_ganggang_ui")
        #self.assertEqual(json_result["jobs"][-1]["name"], "test_ggang_demo")
        pass
    def tearDown(self):
        print "end"

if __name__ =="__main__":
    unittest.main()