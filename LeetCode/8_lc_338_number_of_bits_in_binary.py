import math
from typing import List

"""
https://leetcode.com/problems/counting-bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Solution -  Runtime : 6.9%
            Memory  : 5.7% 

"""
class Solution:
    def calculate_bits(self, n: int) -> int:
        count = 0
        for i in range(int(math.log(n, 2))+1):
            d = 1 << i
            if d & n:
                count += 1
        return count

    def countBits(self, n: int) -> List[int]:
        bit_array = [0]
        for i in range(1, n+1):
            bit_array.append(self.calculate_bits(i))
        return bit_array

    def neetcode(self,  n: int) -> List[int]:
        dp = [0] * (n+1)
        last_pow = 1
        for i in range(1, n+1):
            if i == 1:
                dp[i] = 1
            if i == last_pow * 2:
                last_pow *=  2
            dp[i] = dp[i - last_pow] + 1

        return dp

    def find_recursive_bin(self, dp: List[int], i: int, pow : int, last: int):
        if i == pow*2:
            pow *= 2
        if i == last:
            return
        elif i == 1:
            dp[i] = 1
        if i == 0:
            dp[i] = 0
        else:
            dp[i] = 1 + dp[i-pow]
        self.find_recursive_bin(dp, i+1, pow, last)


    def neetcode_2(self, n: int) -> List[int]:
        """
        This is a recursive approach to the problem
        """

        dp = [0] * (n+1)
        self.find_recursive_bin(dp, 1, 1, n+1)
        return dp


print(Solution().neetcode_2(0))
