import unittest
from BackTracking.nQueens_problem import is_queen_safe, NQueens


class TestnQueens(unittest.TestCase):
    def setUp(self) -> None:
        NQueens.positive_diagonals = {3, 2}
        NQueens.negative_diagonals = {-3, 0}
        NQueens.column_indices = {0, 1}

    def test_is_queen_safe_true(self, ) -> None:

        self.assertTrue(is_queen_safe(2, 4))

    def test_is_queen_safe_false(self, ):

        self.assertIs(is_queen_safe(2, 1), False)



if __name__ =="__main__":
    unittest.main()
