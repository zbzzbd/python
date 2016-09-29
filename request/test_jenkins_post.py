import json
import unittest
import requests

class test_jenkins_post(unittest.TestCase):

    def setUp(self):
        self.bulid_job_url = 'http://localhost:8080/jenkins/job/test_ggang_demo/build'
        self.disable_job_rul='http://localhost:8080/jenkins/job/test_ggang_demo/disable'
        self.job_url ='http://localhost:8080/jenkins/job/test_ggang_demo/api/json'

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


    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()
