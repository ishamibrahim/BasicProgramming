from typing import List
"""
https://leetcode.com/problems/majority-element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        The solution uses an approach that works with O(1) space complexity
        It takes two variables and increments or decrements based on an element occurence
        If the count goes below 0 it replaces with the new element
        This is called the Booyer moore algorithm. This only works if the majority element occurs more than n/2 times

        Solution:   runtime : 92%
                    Memory : 28.5%
        """
        max_count = 0
        max_ele = nums[0]
        for i in nums:
            max_count = max_count + 1 if i == max_ele else max_count - 1
            if max_count == -1:
                max_ele = i
                max_count = 1
        return max_ele


print(Solution().majorityElement([2,2,1,1,1,2,2]))
