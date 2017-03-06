import json
import unittest
import requests

class test_jenkins_post(unittest.TestCase):

    def setUp(self):
        self.job_url ='http://192.168.0.213:8080/jenkins/job/test_exe/lastSuccessfulBuild/api/json?pretty=true'
    """
    def test_build_job(self):
        r= requests.post(self.bulid_job_url,data={},auth=('zbzzbd','zbzzbd'))
        print r.status_code
        self.assertEqual(r.status_code,201)

    def test_disable_job(self):
        job_info=requests.get(self.job_url,auth=('zbzzbd','zbzzbd')).json()
        print job_info["buildable"]
        #self.assertEqual(job_info["buildable"],"True")
        self.assertTrue(job_info["buildable"])
        r = requests.post(self.bulid_job_url,data={},auth=('zbzzbd','zbzzbd'))
        self.assertEqual(r.status_code,201)

    """

    def test_get_data_job(self):
        job_info = requests.get(self.job_url,auth=('zbzzbd','zbzzbd')).json()
        print job_info
        job_data=json.dumps(job_info)
        print type(job_data)
        data=json.loads(job_data)
        print data["actions"][1]["failCount"]
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()
