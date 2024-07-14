"""
    --medium--
    https://leetcode.com/problems/combinations
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
"""
from typing import List


class Solution:
    """
        The solution uses a backtracking method
        Runtime: 82%
        MEmory: 75%
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        input_nums = [i for i in range(1, n+1)]

        def dfs(start, temp_list):
            if len(temp_list) == k:
                result.append(temp_list.copy())
            else:
                for i in range(start, n):
                    temp_list.append(input_nums[i])
                    dfs(i+1, temp_list)
                    temp_list.pop()
        dfs(0, [])
        return result

print(Solution().combine(5, 3))


