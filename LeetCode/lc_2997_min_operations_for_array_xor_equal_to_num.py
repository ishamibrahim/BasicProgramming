"""
    --medium--
    https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k
    Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.
    Ex:Input: nums = [2,1,3,4], k = 1
    Output: 2
    Explanation: flip 0th bit of 2 to convert to 3 : flip no. 1
                 flip 3rd bit of 4 to convert to 0 : flip no. 2
                 XORing 3 XOR 1 XOR 3 XOR 0 = 1 == k
                 Hence minimum 2 flips required

    Solution:   Runtime - 71%
                Memory  - 82%
"""

from typing import List


class Solution:
    @staticmethod
    def get_binary_len(num):
        # bin() converts num to a binary string value prefixed with '0b', that's why the '-2' at the end
        return len(bin(num)) - 2

    def get_flips_required(self, result: int, k: int):
        count = 0
        for i in range(max(Solution.get_binary_len(result), Solution.get_binary_len(k))):
            comparator = 1 << i
            if not(comparator & result) and (comparator & k):
                count += 1
            if (comparator & result) and not (comparator & k):
                count += 1
        return count

    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        flip_required = self.get_flips_required(result, k)

        return flip_required

print(Solution().minOperations([2,4,4,0], 8))
