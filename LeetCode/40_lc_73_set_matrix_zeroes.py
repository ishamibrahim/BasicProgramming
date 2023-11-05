from typing import List
"""
    --medium--
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    Solution: 
        Runtime - 92%
        Memory - 72%
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_x_positions = set()
        zero_y_positions = set()
        len_y = len(matrix)
        len_x = 0
        if len_y:
            len_x = len(matrix[0])

        for i in range(len_y):
            for j in range(len_x):
                if matrix[i][j] == 0:
                    zero_x_positions.add(j)
                    zero_y_positions.add(i)

        if zero_x_positions:
            for j in zero_x_positions:
                for i in range(len_y):
                    matrix[i][j] = 0
        if zero_y_positions:
            for i in zero_y_positions:
                for j in range(len_x):
                    matrix[i][j] = 0
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)
