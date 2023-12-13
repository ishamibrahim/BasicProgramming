from typing import List
"""
--hard--
https://leetcode.com/problems/similar-string-groups/description/
Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping 
at most two letters (in distinct positions) within the string X.
We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

Solution    -   99.4% in Runtime
            -   17.78% in Memory
"""

class Solution:

    def numSimilarGroups(self, strs: List[str]) -> int:
        len_strs = len(strs)
        done = [False] * len_strs
        match_count = 0

        def find_matching(index):
            nonlocal match_count
            nonlocal done
            index_str = strs[index]
            for i in range(len_strs):
                if not done[i]:
                    delta = 0
                    for a, b in zip(index_str, strs[i]):
                        if a != b:
                            delta += 1
                        if delta > 2:
                            break
                    else:
                        match_count += 1
                        done[i] = True
                        find_matching(i)

        for i in range(len(strs)):
            if not done[i]:
                done[i] = True
                find_matching(i)
        return len_strs - match_count


print(Solution().numSimilarGroups(["tars","rats","arts","star"]))

