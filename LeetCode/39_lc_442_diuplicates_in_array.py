from typing import List
"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer 
appears once or twice, return an array of all the integers that appears twice.

Solution:
    Runtime - 95%
    Memory  - 45%
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count_dict = {}
        result_list = []
        for num in nums:
            count_dict[num] = 1 if not count_dict.get(num, 0) else count_dict[num] + 1
        for num, count in count_dict.items():
            if count > 1:
                result_list.append(num)
        return result_list


print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
