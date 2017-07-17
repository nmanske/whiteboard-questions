''' Python test template
'''

import unittest

def check_problem(data):
    return None

class TestProblem(unittest.TestCase):

    problem_data = None

    def test_problem(self):
        # problem check
        result = check_problem(self.problem_data)
        self.assertEquals(result, None)
        #self.assertTrue(result)
        #self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

