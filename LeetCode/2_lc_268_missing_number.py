"""
--easy--
https://leetcode.com/problems/missing-number/
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
            Runtime : 41%
            Memory : 60%
        """
        n_len = len(nums)
        missing = n_len
        sorted_nums = sorted(nums)
        count = 0
        for i in sorted_nums:
            if i !=count:
                missing = count
                break
            count+= 1
        return missing

    def missingNumber2(self, nums: List[int]) -> int:
        """
            Runtime : 5%
            Memory : 17%
        """
        count = 0
        missing = pow(9, 9)
        while count < len(nums)+1:
            if count not in nums:
                missing = count
                break
            count+= 1
        return missing


    def missingNumber3(self, nums: List[int]) -> int:
        """
            Runtime : 15%
            Memory : 60 %
        """
        for count in range( len(nums)+1):
            try:
                nums.remove(count)
            except Exception as e:
                return count
    def missing_number_4(self, nums: List[int])-> int:
        """
            Compars sum of nums and sum of range(nums)
            Runtime: 90%
            Memory: 32%
        """
        total = sum(nums)
        og_total = sum(range(len(nums)+1))
        return og_total - total

    def neetcode(self, nums: List[int]) -> int:
        """
        Uses XOR strategy, any number XORd with itself results to 0. and the missing number will remain
        Runtime: 91%
        Memory : 32%
        """
        result = 0
        for i in range(len(nums)):
            result = result ^ nums[i]
            result = result ^ i

        result = result ^ len(nums)
        return result



print(Solution().neetcode([9,6,4,2,3,5,7,0,1]))
