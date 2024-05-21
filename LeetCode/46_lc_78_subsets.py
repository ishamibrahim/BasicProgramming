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

    def find_subsets(self, i, nums, final_list, init_list):
        final_list.append(init_list.copy())
        for j in range(i, len(nums)):
            init_list.append(nums[j])
            self.find_subsets(j+1, nums, final_list, init_list)
            init_list.pop()


    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
            This uses greedy method
            Runtime: 72%
            Memory:77%
        """
        subset_list = []
        self.find_subsets(0, nums, subset_list, [])
        return subset_list

nums = [1,2, 3, 4]
print(Solution().subsets(nums))


