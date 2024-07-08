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
        with O(1) space used.
        """
        nums.sort()
        minim = float("INF")
        for i in range(len(nums)-1):
            minim = min(minim, nums[i+1] - nums[i] )
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i]  == minim:
                print(nums[i], nums[i+1])

Solution().print_minimum_difference( [2, 15, 7, 4, 10, 13])
