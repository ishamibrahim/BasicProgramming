"""
--easy--

https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Converts list to a set
        Runtime : 97%
        Memory: 8.4%

        """
        newset = set(nums)
        if len(newset) < len(nums):
            return True
        else:
            return False


    def containsDuplicate2(self, nums: List[int]) -> bool:
        """
        Uses dict to get the first duplicate item
        Runtime : 73%
        Memory: 26%
        """
        nums_dict = dict()
        for i in nums:
            if not nums_dict.get(i, None):
                nums_dict[i] = 1
            else:
                return True
        return False




print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(Solution().containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))
