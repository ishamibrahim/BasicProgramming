from typing import List
"""
    --easy--
    Given an integer array nums consisting of n elements, and an integer k.
    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
    Ex: nums = [1,12,-5,-6,50,3], k = 4
        Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    
    Solution -  Runtime  93.2%
                Memory 50%
"""



class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Instead of finding max via sum(List) method.  we calculate for faster performance
        """
        current_sum = sum(nums[:k-1])
        max_sum = -float("INF")
        for i in range(k-1, len(nums)):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[i-k+1]
        return max_sum / k

print(Solution().findMaxAverage([3],1))
