import unittest
from odd_or_even import is_odd 

class Test_is_odd_or_even(unittest.TestCase):
    
    

    def test_pass10_reports_eveni(self):
       self.assertTrue(is_odd(10))

if __name__ == '__main__':
    unittest.main()
