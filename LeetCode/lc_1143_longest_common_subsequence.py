import itertools
"""
https://leetcode.com/problems/longest-common-subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
Example 1:

Input: text1 = "abcde", text2 = "acle" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            Solution is from neetcode, uses dynamic programming, it creates a 2D matrix of incremental values from bottom up
            If both letters match, the value is incremented one from its diagonal cell.
            Hence, matrix[i][j] = 1 + matrix[i+1][j+1]
            Otherwise duplicates will be considered

            Runtime: 84%
            Memory: 79%


        """
        matrix = [[0] * (len(text1)+1) for _ in itertools.repeat(None, len(text2)+1)]
        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[0])-2, -1, -1):
                if text2[i] == text1[j]:
                    matrix[i][j] = 1 + matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i+1][j], matrix[i][j+1])
        return matrix[0][0]



print(Solution().longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr"))
print(Solution().longestCommonSubsequence("abcde", "acle"))
