from str_match_unique import StrTest
import unittest


class StringTesting(unittest.TestCase):

    def setUp(self):
        self.s1 = "abc"
        self.s2 = "bcd"

    def testString(self):
        str_obj = StrTest(self.s1, self.s2)
        self.assertEqual("bc", str_obj.common())
        self.assertEqual("ad", str_obj.unique())


if __name__ == '__main__':
    unittest.main()
