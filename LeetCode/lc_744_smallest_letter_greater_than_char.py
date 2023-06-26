"""
--easy--
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.

"""
from typing import List


class Solution:

    def binary_search(self, letters: List[str], front, back :int, target: str) -> str:
        if front < back :
            mid = (front+back)//2
            if 1 <= mid < len(letters) and letters[mid] > target >= letters[mid - 1]:
                return letters[mid]
            elif mid == 0:
                return letters[mid]
            else:
                if letters[mid] < target:
                    return self.binary_search(letters, mid+1, back, target)
                else:
                    return self.binary_search(letters, front, mid, target)
        return letters[0]

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target:
            return letters[0]
        else:
            return self.binary_search(letters, 0, len(letters), target)


print(Solution().nextGreatestLetter(["c", "f", "j"], "d"))
