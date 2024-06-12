"""
--medium--
https://leetcode.com/problems/permutations/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Ex:Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            The solution uses backtracking. Removes each item and sends it to the next recursive call
            Runtime: 99%
            Memory: 35%
        """
        result = []
        def fetch_permutations(nums_new: List[int], adapted_nums:List[int]):
            if nums_new:
                nums_len = len(nums_new)
                for _ in itertools.repeat(None, nums_len):
                    new_num = nums_new.pop(0)
                    adapted_nums.append(new_num)
                    fetch_permutations(nums_new, adapted_nums)
                    nums_new.append(new_num)
                    adapted_nums.pop(-1)
            else:
                result.append(adapted_nums[:])
        fetch_permutations(nums, [])
        return result

print(Solution().permute([1, 2, 3, 4]))
