"""
--medium--
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest in s.
Ex: Input: s = "babad"
Output: "bab"
Ex: Input: s = "cakeddee"
output: "edde"

Solution    -   15.3% in Runtime
            -   83% in Memory
        TODO: Needs improvement
"""


class Solution:
    def is_palindrome(self, subs: str, start, end: int):
        if start < end:
            if subs[start] == subs[end]:
                return self.is_palindrome(subs, start+1, end-1)
            else:
                return False
        else:
            return True


    def longestPalindrome(self, s: str) -> str:
        largest_sub = ""
        for i in range(len(s)-1):
            for j in range(len(s)-1, 0, -1):
                if (j-i) < len(largest_sub):
                    break
                if i < j:
                    if s[i] == s[j]:
                        subs = s[i:j+1]
                        if self.is_palindrome(s, i, j):
                            if len(subs) > len(largest_sub):
                                largest_sub = subs
                                break
                else:
                    break

        if not largest_sub:
            largest_sub = s[0]

        return largest_sub

s = "babad"
print(Solution().longestPalindrome(s))
