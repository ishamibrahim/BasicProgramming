from typing import List

"""
https://leetcode.com/problems/squares-of-a-sorted-array
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        This solution uses two parts
        1st parts finds the closes number to 0 using binary search
        2nd part uses front and back pointer to traverse through the list with pointers moving forward and backward respectively

        Solution -  Runtime: 30.6%
                    Memory: 21.7%
        """
        # Part I
        l_nums = len(nums)
        low = 0
        high = l_nums
        front = 0
        results = []
        while True:
            mid = (low+high) // 2
            if mid:
                if mid == l_nums - 1:
                    if nums[mid] >= 0:
                        front = mid
                    else:
                        front = l_nums
                    break
                if nums[mid] == 0:
                    front = mid
                    break
                if nums[mid] >= 0 and nums[mid-1] < 0:
                    front = mid
                    break
                if nums[mid] > 0:
                    high = mid
                else:
                    low = mid
            else:
                break
        # Part II
        back = front -1
        count = 0
        while count < l_nums:
            if back >= 0 and front < l_nums:
                back_num = abs(nums[back])
                if back_num < nums[front]:
                    results.append(pow(back_num, 2))
                    back -=1
                else:
                    results.append(pow(nums[front], 2))
                    front += 1
            elif front == l_nums:
                results.append(pow(nums[back], 2))
                back -=1
            else:
                results.append(pow(nums[front], 2))
                front += 1
            count += 1
        return results

    def neetcode(self, nums: List[int]) -> List[int]:
        """
        This solution places two pointers at each end of the list and compare the two
        the result is added in decreasing order starting from the largest

        Solution -  Runtime: 75%
                    Memory: 21.7%
        """
        l_nums = len(nums)
        front, back = 0, l_nums-1
        results = [0] * l_nums
        count = 1
        while front <= back:
            if abs(nums[front]) > abs(nums[back]):
                number = nums[front]
                front += 1
            else:
                number = nums[back]
                back -= 1
            results[-count] = number*number
            count += 1
        return results


print(Solution().neetcode([-5, -3, -1, 2, 4, 9]))
