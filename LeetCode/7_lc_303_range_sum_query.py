from typing import List
"""
-easy-
https://leetcode.com/problems/range-sum-query-immutable
Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Solution -      Timeout exceeded

"""

import math
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        self.calculate_prefix(nums)

    def calculate_prefix(self, nums):
        last_sum = 0
        for num in nums:
            last_sum += num
            self.prefix.append(last_sum)

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])

    def neetcode(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix[right] - self.prefix[left-1]
        else:
            return self.prefix[right]



n = NumArray([-2,0,3,-5,2,-1])
print(n.prefix)
print(n.sumRange(0, 2))
