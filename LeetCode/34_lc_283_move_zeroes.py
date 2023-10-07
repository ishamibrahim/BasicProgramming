from typing import List
"""
--easy--
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        The solution uses an approach like selection insertion sort
        Runtime : 5%
        """
        #Do not return anything, modify nums in-place instead.
        l_nums = len(nums)
        fst, lst = 0, l_nums - 1
        while fst < lst:
            if nums[fst] == 0:
                temp_ind = fst
                while temp_ind < lst:
                    nums[temp_ind] = nums[temp_ind+1]
                    temp_ind += 1
                nums[lst] = 0
                lst -= 1
            else:
                fst += 1

    def find_0_index_in_list(self, nums, base_ind):
        """

        """
        base_ind += 1
        while  base_ind < len(nums) and nums[base_ind] != 0:
            base_ind += 1
        return base_ind

    def find_non_0_index_in_list(self, nums, base_ind):
        base_ind += 1
        while  base_ind < len(nums) and nums[base_ind] == 0:
            base_ind += 1
        return base_ind

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        This approach searches first 0 and first non-zero number and swaps it
        until the end is reached
        Runtime: 5%
        """
        l_nums = len(nums)
        fst, lst = -1, -1
        while fst < l_nums and lst < l_nums:
            fst = self.find_0_index_in_list(nums, fst)
            lst = self.find_non_0_index_in_list(nums, fst)
            if fst < l_nums and lst < l_nums:
                nums[fst], nums[lst] = nums[lst], nums[fst]

    def neetCode(self, nums: List[int]) -> None:
        """
        The solution finds the non-zero number one by one and shifts it to left side
        Runtime: 90%
        """
        l = -1
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
            r += 1


numss = [0, 1, 0, 3, 12, 0, 25, 0]

Solution().neetCode(numss)
print(numss)

l = [1, 2, 3]
print(id(l))
l.reverse()
print(id(l))
print(l)

