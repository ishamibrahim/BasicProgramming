from typing import List

"""
https://leetcode.com/problems/single-number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Solution:
Solution    -   64.3% in Runtime
            -   75.5% in Memory

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0

        nums.sort()
        result = nums[i]
        while(i < len(nums)-1):
            if nums[i] == nums[i+1]:
                i += 2
            else:
                result= nums[i]
                break
        return result

    def from_neetcode(self, nums: List[int]) -> int:
        result = 0
        for elem in nums:
            result = result ^ elem

        return result




print(Solution().singleNumber([3, 5, 7, 3, 5]))

