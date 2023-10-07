class Solution:
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    Ex: s = "abc", t = "ahbgdc" ==> True
        s = "axc", t = "ahbgdc" ==> False

    Solution:   Runtime: 95%
                Memory : 62%
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        small, large = 0, 0
        is_found = False
        len_s = len(s)
        while small < len_s and large < len(t):
            if s[small] == t[large]:
                small += 1
                large += 1
            else:
                large += 1
        if small == len_s:
            is_found = True
        return is_found

print(Solution().isSubsequence("abc", "ahbgdc"))

