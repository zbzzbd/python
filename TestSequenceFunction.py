import unittest

def div(a,b):
    return a/b

class TestSequenceFunction(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_set(self):
        print "test case"


    def test_3_div_4(self):
        self.assertEqual(div(3/4),3/4)

    def test_3_div_0(self):
        self.assertRaises(ZeroDivisionError,div,3,0)

    def tearDown(self):
        print 'after every test case'

if __name__ =='__main__':
    unittest.main()