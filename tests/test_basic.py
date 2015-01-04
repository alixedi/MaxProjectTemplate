import unittest

class TestBasic(unittest.TestCase):

    def test_basic(self):
        self.assertTrue(2+1==3)

if __name__ == '__main__':
    unittest.main()
