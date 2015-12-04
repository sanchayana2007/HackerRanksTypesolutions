__author__ = 'Sanchayan'

import unittest
#from unnecessary_math import multiply

def multiply(a,b):
    return a*b

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)

    def test_numbers_3_4(self):
        self.assertNotEqual( multiply(3,4), 14)

    def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

'''


class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
'''
if __name__ == '__main__':
    unittest.main()