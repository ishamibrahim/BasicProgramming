from typing import List
"""
https://leetcode.com/problems/convert-1d-array-into-2d-array/
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. 
You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

Solution - Runtime: 84%
            Memory: 11%
"""

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        k = 0
        len_original =len(original)
        product = m*n
        if product < len_original:
            return result
        elif product > len_original:
            return result
        for i in range(m):
            inner_list = []
            for j in range(n):
                inner_list.append(original[k])
                k += 1
            result.append(inner_list)

        return result


print(Solution().construct2DArray([1,2, 3, 4, 5], 1,3))
