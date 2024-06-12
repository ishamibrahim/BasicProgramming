import heapq
import itertools
from typing import List
"""
    --medium--
    https://leetcode.com/problems/top-k-frequent-elements/
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            Solution uses a dictionary that keeps count of numbers on parsing the list
            Runtime: 84%
            Memory: 39%
        """
        count_dict = {}
        for num in nums:
            if count_dict.get(num):
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        count_tuples = [(val, count) for val, count in count_dict.items()]
        count_tuples.sort(key=lambda x: x[1], reverse=True)
        counts = [x[0] for x in count_tuples]
        return counts[:k]


    def neetcode(self, nums: List[int], k: int) -> List[int]:
        """
            Solution uses a dictionary that keeps count of numbers on parsing the list
            Runtime: 84%
            Memory: 39%
        """
        count_dict = {}
        counts_list = [[] for _ in range(len(nums)+1)]
        final_list = []
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)

        for val, count in count_dict.items():
            counts_list[count].append(val)

        for ind in range(len(counts_list)-1, 0, -1):
            for count in counts_list[ind]:
                final_list.append(count)
                if len(final_list) == k:
                    return final_list




print(Solution().neetcode([1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 3, 3, 3, 3, 3, 3, 3], 2))

