"""
Akam question for SSE2

Given a list of integers, print all the numbers that have the minimum difference.
Ex : nums = [2, 15, 7, 4, 10, 13]
    Result:  2 4
            13 15
"""
from typing import List


class Solution:
    def print_minimum_difference(self, nums: List[int]):
        """
        Solution uses O(n log n) time for sorting and O(n) time for the algorithm
        with O(1) space used exclusive of final_list
        """
        nums.sort()
        minim = float("INF")
        previous_min = minim
        final_list = []
        for i in range(len(nums)-1):
            minim = min(minim, nums[i+1] - nums[i])
            if minim != previous_min:
                final_list = [(nums[i], nums[i+1])]
                previous_min = minim
            else:
                if nums[i+1] - nums[i] == minim:
                    final_list.append((nums[i], nums[i+1]))
        return final_list

print(Solution().print_minimum_difference( [2, 15, 7, 4, 10, 13]))
