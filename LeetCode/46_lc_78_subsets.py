import itertools
from typing import List
"""
--medium--
https://leetcode.com/problems/subsets
Given an integer array nums of unique elements, return all possible subsets withotu duplicates in any arrangement.
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""

class Solution:

    def find_subsets(self, i, nums, num_len, final_list, init_list):
        final_list.append(init_list[:])
        for j in range(i, num_len):
            init_list.append(nums[j])
            self.find_subsets(j+1, nums, num_len, final_list, init_list)
            init_list.pop()


    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
            This uses backtracking method
            Runtime: 72%
            Memory:77%
        """
        subset_list = []
        num_len = len(nums)
        self.find_subsets(0, nums, num_len, subset_list, [])
        return subset_list

    def add_item(self, nums, iter, result, num_len):
        temp = []
        for i in range(num_len):
            if iter & (1 << i):
                temp.append(nums[i])
        result.append(temp)

    def subsets2(self, nums: List[int])-> List[List[int]]:
        """
            This uses bit masking method
            Runtime: 72%
            Memory:8%
        """
        result = []
        count = 0
        num_len = len(nums)
        for _ in itertools.repeat(None, pow(2, num_len)):
            self.add_item(nums, count, result, num_len)
            count += 1
        return result

nums = [1,2,3, 4]
print(Solution().subsets1(nums))

