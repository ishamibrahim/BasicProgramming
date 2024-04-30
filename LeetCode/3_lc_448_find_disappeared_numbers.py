"""
- Easy -
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
range [1, n] that do not appear in nums.

Solution    -   79.3% in Runtime
            -   07.5% in Memory
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:

        new_list = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                new_list.append(i)
        return new_list

    def findDisappearedNumbers3(self, nums: List[int]) -> List[int]:
        """
            Uses dictionary to initialize all numbers. This takes extra space to create a dictionary
            Runtime : 95%
            Memory: 15%
        """
        integer_dict = {i: True for i in range(1, len(nums)+1)}
        for num in nums:
            if integer_dict.get(num, None):
                integer_dict.pop(num)

        return list(integer_dict.keys())

    def  neetcode(self, nums: List[int]) -> List[int]:
        """
            This uses O(1) space since it does not create a new space.
            Here numbers corresponding to their respective -1 locations are negated, which means positions related to missing numbers remain positive

            Runtime: 27%
            Memory: 79%
        """
        for num in nums:
            i = abs(num) -1
            nums[i] = -1 * abs(nums[i])

        result = []
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i+1)
        return result

l1 = [5, 1, 4, 3, 1]
print(Solution().neetcode(l1))

