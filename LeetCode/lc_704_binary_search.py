"""
https://leetcode.com/problems/binary-search/
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

Solution -  Runtime : 90%
            Memory: 5.8%
"""
from typing import List


class Solution:
    def search_indexes(self, front,  back: int, nums: List[int], target: int):
        if front < back:
            mid = (front + back) // 2
            if nums[mid] == target:
                return mid
            else:
                if target < nums[mid]:
                    return self.search_indexes(front, mid, nums, target)
                else:
                    return self.search_indexes(mid+1, back, nums, target)
        return -1

    def search(self, nums: List[int], target: int) -> int:
        front = 0
        back = len(nums)
        return self.search_indexes(front, back, nums, target)


print(Solution().search([9], 9))
