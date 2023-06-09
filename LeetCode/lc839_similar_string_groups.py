from typing import List


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





print(Solution().numSimilarGroups(["wwq", "wqw", "qww"]))
print(2/2)

