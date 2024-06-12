import itertools
from typing import List

class Solution:
    """
    --medium--
    https://leetcode.com/problems/permutations-ii/
    Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
    Ex: Input: nums = [1,1,2]
        Output: [[1,1,2], [1,2,1], [2,1,1]]
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
            The solution is from neetcode.
            It is a backtracking algorithm that uses DFS and  a dict that stores the number of items per item to avoid duplicates.
            Runtime: 88%
            Memory: 75%
        """

        result = []
        num_dict = {}
        perm_list = []
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1

        def fetch_unique_permutations():
            if len(perm_list) == len(nums):
                result.append(perm_list[:])
            for num in num_dict.keys():
                if num_dict[num]:
                    num_dict[num] -= 1
                    perm_list.append(num)
                    fetch_unique_permutations()
                    perm_list.pop()
                    num_dict[num] += 1
        fetch_unique_permutations()
        return result


print(Solution().permuteUnique([1, 1, 3]))
