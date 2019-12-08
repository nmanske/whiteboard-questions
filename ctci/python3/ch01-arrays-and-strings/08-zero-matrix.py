'''Write an algorithm such that if an element in an MxN matrix is 0, its entire
row and column are set to 0.'''

import unittest

def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    zero_rows = []
    zero_cols = []

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                zero_rows.append(row)
                zero_cols.append(col)

    for row in zero_rows:
        clear_row(matrix, row)

    for col in zero_cols:
        clear_col(matrix, col)

    return matrix

def clear_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def clear_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ]),
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
