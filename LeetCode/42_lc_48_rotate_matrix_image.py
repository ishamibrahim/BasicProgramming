"""
--medium--
https://leetcode.com/problems/rotate-image/description/
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
Modify the matrix directly without creating a new matrix
Ex: input =     [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                ]
Output: [[7,4,1],
        [8,5,2],
        [9,6,3]]

"""
from typing import List
from utils import print_matrix

MOVEMENT_CORDS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def switch_next_item(self, matrix, src_number, cur_y, cur_x, movement_index, move_step_start, move_step_end):
        count = 1
        while count < (move_step_end - move_step_start) :
            new_y = cur_y + MOVEMENT_CORDS[movement_index][0]
            new_x = cur_x + MOVEMENT_CORDS[movement_index][1]
            if not (move_step_start <= new_y < move_step_end) or not (move_step_start <= new_x < move_step_end):
                movement_index = (movement_index + 1) % len(MOVEMENT_CORDS)
                continue
            else:
                count += 1
                cur_y, cur_x = new_y, new_x

        temp_var = matrix[cur_y][cur_x]
        matrix[cur_y][cur_x] = src_number
        return temp_var, movement_index, cur_y, cur_x

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Solution :
            Runtime - 50%
            Memory  - 59%
        """

        len_matrix = len(matrix)
        direction = 0
        no_of_rounds = len_matrix
        for next_y in range(len_matrix-no_of_rounds, len_matrix//2):
            for next_x in range(len_matrix-no_of_rounds, no_of_rounds-1):
                next_item = matrix[next_y][next_x]
                for _ in range(4):
                    next_item, direction, next_y, next_x = self.switch_next_item(matrix, next_item, next_y, next_x, direction, len_matrix-no_of_rounds, no_of_rounds)
            no_of_rounds -= 1


square_matrix = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]
Solution().rotate(square_matrix)
print_matrix(square_matrix)

"""
# Solution II
# Runtime: 82%
# MEmory: 20% 
    direction_coords = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    border_coords = [(0, 1), (1, 1), (1, 0), (0, 0)]

    def get_next_pos(self, direction_ind, iter_count, circle_count, matrix_len):
        dir_y, dir_x = self.direction_coords[direction_ind]
        bor_y, bor_x = self.border_coords[direction_ind]

        next_y =circle_count + (matrix_len - 1) * bor_y + (iter_count * dir_y)
        next_x =circle_count + (matrix_len - 1) * bor_x + (iter_count * dir_x)

        return next_y, next_x

    def rotate_circle(self, cur_y, cur_x, circle_count, matrix_len, in_matrix):
        direction_ind = 0

        for i in range(matrix_len - (circle_count * 2) - 1):
            cur_x = circle_count + i
            changer = in_matrix[cur_y][cur_x]
            for j in range(4):
                next_y, next_x = self.get_next_pos(direction_ind, i, circle_count, (matrix_len-circle_count*2))
                direction_ind = (direction_ind + 1) % 4
                temp = in_matrix[next_y][next_x]
                in_matrix[next_y][next_x] = changer
                changer = temp
                cur_y, cur_x = next_y, next_x

    def rotate(self, in_matrix: List[List[int]]):
        matrix_len = len(in_matrix)
        circle_count = 0
        while circle_count < matrix_len // 2:
            cur_y = cur_x = circle_count
            self.rotate_circle(cur_x, cur_y, circle_count, matrix_len, in_matrix)
            circle_count += 1
"""
