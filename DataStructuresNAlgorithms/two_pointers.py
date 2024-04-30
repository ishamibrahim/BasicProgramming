"""
Two pointer technique is an efficient technique for searching pairs over SORTED array

"""
from typing import List


class Sol:
    list_a = [10, 20, 35, 50, 75, 80]

    """
        Problem: Find two indices where the sum two items in a sorted list is equal to certain value
    """
    def get_two_indices_for_sum(self, sum_to_find):
        len_list = len(self.list_a)
        left = 0
        right = len_list-1
        while left < len_list and right >= 0:
            current_sum = self.list_a[left] + self.list_a[right]
            if current_sum == sum_to_find:
                return left, right
            elif current_sum < sum_to_find:
                left += 1
            else:
                right -= 1
        return None, None


    def move_all_zeroes_to_the_end(self, in_array: List[int]):
        len_list = len(in_array)
        left = 0
        right = len_list - 1
        while left < len_list and left < right:
            if in_array[left] == 0 and in_array[right] != 0:
                in_array[left], in_array[right] = in_array[right], in_array[left]
                left += 1
                right -= 1
            elif in_array[left] == 0:
                right -= 1
            else:
                left += 1
        return in_array





solution = Sol()
# print(solution.get_two_indices_for_sum(70))
print(solution.move_all_zeroes_to_the_end([8, 0, 9, 0, 1, 2, 3, 0]))





