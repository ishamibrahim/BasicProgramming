"""
---medium--
Given an m x n matrix, return all elements of the matrix in spiral order.

[[1,  2,   3,  4,  5],
[6,  7,   8,  9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]]
Result : [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
"""
from typing import List
MOVEMENT_LIST = [(0,1), (1, 0), (0, -1), (-1, 0)]
LEN_MOVES = len(MOVEMENT_LIST)


class Solution:
    """
    Solution:
        Runtime: 90%
        Memory: 62%
    """
    def add_next_item(self, l_ind, r_ind, matrix, bool_matrix, spiral_list, prev_direction_index):
        spiral_list.append(matrix[l_ind][r_ind])
        bool_matrix[l_ind][r_ind] = True
        for i in range(LEN_MOVES):
            direction_ind = (prev_direction_index + i) % LEN_MOVES
            add_i, add_j = MOVEMENT_LIST[direction_ind]
            try:
                if not bool_matrix[l_ind+add_i][r_ind+add_j]:
                    self.add_next_item(l_ind+add_i, r_ind+add_j, matrix, bool_matrix, spiral_list, direction_ind)
                    return
            except IndexError:
                continue

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        bool_matrix = [[False for x in matrix[0]] for y in matrix]
        spiral_list = []
        self.add_next_item(0, 0, matrix, bool_matrix, spiral_list, 0)
        print(spiral_list)
        return spiral_list


Solution().spiralOrder([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
