#-*- coding:utf-8 -*-
import  unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        print("test case start")

    @unittest.skip
    def test_skip(self):
        print("aaaaaa")

    @unittest.skipIf(3>2,"当条件满足则跳过")
    def test_skip_if(self):
        print("bbbb")

    @unittest.skipUnless(3>2,"当条件满足时执行测试")
    def test_skip_unless(self):
        print("ccccc")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2,3)

    def tearDown(self):
        print("testCase end")

if __name__=='__main__':
    unittest.main()