from typing import List

"""
--hard--
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Solution    -   69.8% in Runtime
            -   55.1% in Memory
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Solution    -   69.8% in Runtime
                    -   55.1% in Memory
        """

        count = 0
        nums1_len = nums1_p = len(nums1)
        nums2_len = nums2_p = len(nums2)
        total_len = nums1_len + nums2_len
        mid_len = total_len//2
        even_len = total_len%2 == 0
        previous = median = 0
        while nums1_p or nums2_p:
            if nums1_p and nums2_p:
                if nums1[nums1_len - nums1_p] < nums2[nums2_len - nums2_p]:
                    current = nums1[nums1_len-nums1_p]
                    nums1_p -= 1
                else:
                    current = nums2[nums2_len-nums2_p]
                    nums2_p -= 1
            elif nums1_p:
                current = nums1[nums1_len-nums1_p]
                nums1_p -= 1
            else:
                current = nums2[nums2_len-nums2_p]
                nums2_p -= 1

            if count == mid_len:
                if even_len:
                    median = (current + previous )/2
                else:
                    median = float(current)
                break
            count+=1
            previous = current

        return median


    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        """
            This uses merge sort technique to merge two lists to one, then finds out the median
            Runtime: 75%
            Memory: 95%

        """

        single_arr = []
        while nums1 or nums2:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    single_arr.append(nums1.pop(0))
                else:
                    single_arr.append(nums2.pop(0))
            elif nums1:
                single_arr.append(nums1.pop(0))
            else:
                single_arr.append(nums2.pop(0))
        median_point = len(single_arr) / 2
        if median_point.is_integer():
            median = (single_arr[int(median_point)] + single_arr[int(median_point)-1])/2
        else:
            median = float(single_arr[int(median_point)])
        return median



print(Solution().findMedianSortedArrays2([1,2, 3, 4], [3,4, 9, 11]))

