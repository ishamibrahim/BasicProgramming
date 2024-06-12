from typing import List
"""
    --medium--
    https://leetcode.com/problems/subsets-ii/
    Given an integer array nums that may contain duplicates, return all possible subsets.
"""


class Solution:
    def find_subsets(self, nums, i, iter_list, result):
        result.append(iter_list)
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue
            self.find_subsets(nums, j+1, iter_list+[nums[j]], result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            Solution uses recursion method with a condition.
            The items are first sorted so that duplicates appear one after the other.
            The idea is that if we consider duplicates only once when it comes in the first index of every recursive call,
            and avoid it in all other iterations.

            Runtime: 80%
            Memeory: 99%

        """
        result = []
        nums.sort()
        self.find_subsets(nums, 0, [], result)
        return result

    def find_subsets2(self, i, nums, num_len, final_list, init_list):
        final_list.append(init_list[:])
        popped_num = float("INF")
        for j in range(i, num_len):
            if popped_num == nums[j]:
                continue
            init_list.append(nums[j])
            self.find_subsets2(j+1, nums, num_len, final_list, init_list)
            popped_num = init_list.pop()


    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        """
            Solution uses backtracking with a condition, that if the popped item
            and the next item are the same, then it skips that iteration.
            Hence adjacent duplicate numbers are considered only once in a loop,
            but are considered in a recursion.

            Runtime: 75%
            Memeory: 90%

        """
        subset_list = []
        num_len = len(nums)
        nums.sort()
        self.find_subsets2(0, nums, num_len, subset_list, [])
        return subset_list

nums = [1, 1, 2, 3]
print(Solution().subsetsWithDup(nums))
print(Solution().subsetsWithDup2(nums))

