from typing import List
"""
https://leetcode.com/problems/two-sum
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        First it creates a dictionary with number and their indices
        then iterates through each number to find the difference.
        Runtime: 86.7%
        Memory: 5.7%
        """
        hashmap = dict()
        for i in range(len(nums)):
            if hashmap.get(nums[i]):
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]

        for num, pos in hashmap.items():
            delta = target - num

            delta_pos = hashmap.get(delta)

            if delta_pos:
                # If delta is same as num, i.e num is half of target
                if delta == num:
                    if len(delta_pos) == 1:
                        continue
                    else:
                        return[pos[0], delta_pos[1]]
                return [pos[0], delta_pos[0]]

print(Solution().twoSum([3,2,4], 6))

