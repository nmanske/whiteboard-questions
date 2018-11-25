''' Python test template
'''

import unittest

def check_problem(data):
    return None

class Test(unittest.TestCase):

    data = None

    def test_problem(self):
        for test in self.data:
            result = check_problem(test)
            self.assertEqual(result, None)
            #self.assertTrue(result)
            #self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
