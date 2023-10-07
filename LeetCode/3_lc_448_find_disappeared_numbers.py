"""
- Easy -
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
range [1, n] that do not appear in nums.

Solution    -   79.3% in Runtime
            -   07.5% in Memory
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        """
        Time limit exceeded
        """
        new_list = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                new_list.append(i)
        return new_list



l1 = [5, 1, 4, 3, 5, 7, 4]
print(Solution().findDisappearedNumbers(l1))

