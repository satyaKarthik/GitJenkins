import testing
import unittest

class unit_testing(unittest.TestCase):
    def test_add(self):
        self.assertEqual(20,testing.add(10,10))
        self.assertEqual(30,testing.add(10,20))
        self.assertEqual(40,testing.add(20,20))
        self.assertEqual(50,testing.add(30,20))
        self.assertNotEqual(30,testing.add(10,30))

    def test_sub(self):
        self.assertEqual(20,testing.sub(30,10))
        self.assertEqual(-40,testing.sub(-20,20))
        self.assertEqual(0,testing.sub(20,20))
        self.assertEqual(-30,testing.sub(20,50))
        self.assertNotEqual(30,testing.sub(10,30))

    def test_mul(self):
        self.assertEqual(300,testing.mul(30,10))
        self.assertEqual(-400,testing.mul(-20,20))
        self.assertEqual(0,testing.mul(0,20))

    def test_div(self):
        self.assertEqual(3,testing.div(30,10))
        self.assertEqual(-1,testing.div(-20,20))
        self.assertEqual(0,testing.div(0,20))
        with self.assertRaises(ValueError):
            testing.div(10,0)

if __name__=="__main__":
    unittest.main()


