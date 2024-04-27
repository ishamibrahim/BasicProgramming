"""
Given a matrix of size m * n of binaries , while each row is sorted, find the row with max 1's\
Ex:
Input :[[0 0 0 1 1 1]
        [0 0 0 0 1 1]
        [0 0 1 1 1 1]
        [0 0 0 0 0 1]]

Output : 3

"""
import time
from typing import List


class Sol:
    ROW = [3, 4, 5, 6]

    def binary_search_for_first_1(self, row):
        f = 0
        l = len(row) - 1
        while True:
            mid = int((f + l) / 2)
            if row[mid]:
                if mid > 0:
                    if not row[mid - 1]:
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
        print(f"Row no. {least_occuring_row} occurs with maximum 1s of count {len_row - least_occuring_ind}")

    ################################################### SECOND ########################################
    def find_max_rows_with_bin_search_pattern(self, in_matrix: List[List[int]]):
        len_matrix = len(in_matrix)
        len_row = len(in_matrix[0])

        start = 0
        end = len_row
        current_matrix_dict = {x: False for x in range(len_matrix)}

        final_len = len_matrix
        while final_len > 1:
            counts = 0
            mid_index = (start + end) // 2
            for row_ind in current_matrix_dict.keys():
                if in_matrix[row_ind][mid_index]:
                    current_matrix_dict[row_ind] = True
                    counts += 1
                else:
                    current_matrix_dict[row_ind] = False

            if counts == 0:
                start = mid_index + 1
            elif counts == len(current_matrix_dict):
                end = mid_index - 1
            else:
                end = mid_index - 1
                final_len = counts
                removable_keys = []
                for key, val in current_matrix_dict.items():
                    if not val:
                        removable_keys.append(key)
                for key in removable_keys:
                    del (current_matrix_dict[key])

        print(current_matrix_dict.items())


binary_matrix = [[0, 0, 0, 0, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 1],
                 [0, 0, 0, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1, 1]]
s = Sol()
start = time.perf_counter()
# s.find_max_in_row(binary_matrix)

s.find_max_rows_with_bin_search_pattern(binary_matrix)
print(f"time taken: {(time.perf_counter() - start):0.7f}")
