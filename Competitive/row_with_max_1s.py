"""
Given a matrix of size m * n of binaries , while each row is sorted, find the row with max 1's\
Ex:
Input :[[0 0 0 1 1 1]
        [0 0 0 0 1 1]
        [0 0 1 1 1 1]
        [0 0 0 0 0 1]]

Output : 2

"""

from typing import List



class Sol:
    ROW = [3, 4, 5, 6]
    for item in ROW:
        print("Testing actions : ", item* item*item)

    def binary_search_for_first_1(self, row):
        f = 0
        l =len(row) - 1
        while True:
            mid = int((f +l) /2)
            if row[mid]:
                if mid > 0 :
                    if not row[mid-1]:
                        return mid
                    else:
                        l = mid - 1
                else:
                    return 0
            else:
                f = mid + 1

    def find_max_in_row(self, in_matrix: List[List[int]]):
        len_matrix = len(in_matrix)
        len_row = len(in_matrix[0])
        least_occuring_ind = float("inf")
        least_occuring_row = float("inf")
        for row in in_matrix:
            row_start_index = self.binary_search_for_first_1(row)
            if row_start_index < least_occuring_ind:
                least_occuring_ind = row_start_index
                least_occuring_row = in_matrix.index(row)
        print(f"Row no. {least_occuring_row} occurs with maximum 1s of count {len_row-least_occuring_ind}")


binary_matrix = [   [0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1],
                    [0, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1]]
s = Sol()
s.find_max_in_row(binary_matrix)



