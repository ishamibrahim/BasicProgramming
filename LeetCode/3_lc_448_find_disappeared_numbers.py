"""
- Easy -
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
range [1, n] that do not appear in nums.

Solution    -   62.3% in Runtime
            -   07.5% in Memory
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        real_set = set(range(1, len(nums)+1))
        return list(real_set - set(nums))


l1 = [2, 1, 2, 5, 6, 7, 1]
print(Solution().findDisappearedNumbers(l1))
