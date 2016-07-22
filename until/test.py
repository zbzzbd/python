import  unittest
from calculator import Count
class TestCount(unittest.TestCase):
    def setUp(self):
        print("test start")
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5,"this add is error")


    def tearDown(self):
        print("test end")
