"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring.
EX:
board = [["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]],
word = "SEE"


"""
from typing import List


class Solution:
    word_found = False
    len_y_board = 0
    len_x_board = 0
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    traversed_matrix = []

    def find_next_letter(self, current, word, y_ind, x_ind, board):
        current += board[y_ind][x_ind]
        self.traversed_matrix[y_ind][x_ind] = True
        # print(f"[{y_ind}][{x_ind}]")
        # print(f"current --> {current}")
        if current == word:
            return True
        if str.startswith(word, current):
            for y, x in self.movements:
                next_y = y_ind + y
                next_x = x_ind + x
                if 0 <= next_x < self.len_x_board and 0 <= next_y < self.len_y_board and not self.traversed_matrix[next_y][next_x]:
                    if self.find_next_letter(current, word, next_y, next_x, board):
                        return True
        self.traversed_matrix[y_ind][x_ind] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            Solution using backtracking

            Runtime - 17%
            Memory - 18%
        """
        self.len_y_board = len(board)
        self.len_x_board = len(board[0])
        self.traversed_matrix = [[False for x in range(self.len_x_board)] for y in range(self.len_y_board)]
        current_word = ""
        for y_ind in range(self.len_y_board):
            for x_ind in range(self.len_x_board):
                if self.find_next_letter(current_word, word, y_ind, x_ind, board):
                    return True
        return False



board = [["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]]
word = "ASAD"
print(Solution().exist(board, word))
