"""
--medium--
Given an integer array nums, return an array 'answer' such that answer[i] is equal to the product of
all the elements of nums except nums[i].
WITHOUT USING DIVISION OPERATOR
"""
import functools
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        This approach is iterating over the list and appending a product of reduce() operation
        Runtime: Timeout
        """
        prod_list = []
        for i in range(len(nums)):
            if i == 0:
                prod1 = 1
                prod2 = functools.reduce(lambda x, y: x*y,  nums[i+1:])
            elif i == len(nums)-1:
                prod1 = functools.reduce(lambda x, y: x*y,  nums[:i])
                prod2 = 1
            else:
                prod1 = functools.reduce(lambda x, y: x*y,  nums[:i])
                prod2 = functools.reduce(lambda x, y: x*y,  nums[i+1:])
            prod_list.append(prod1 * prod2)
        return prod_list

    def neetCode(self, nums: List[int]) -> List[int]:
        """
        Simple approach by multiplying all items pre and post an item one by one
        Create a prefix list first and then multiply it with the postfix items
        Instead of creating two lists for pre and post, use one result list.
        Runtime: 94%
        Memory: 92%

        """
        prod_list = []
        prefix = 1
        l_nums = len(nums)
        for i in range(l_nums):
            prod_list.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(l_nums-1, -1, -1):
            prod_list[i] *= postfix
            postfix *= nums[i]
        return prod_list



print(Solution().productExceptSelf([4, 3, 5, 6, 2]))
print(Solution().neetCode([1, 3, 5, 6, 2]))

