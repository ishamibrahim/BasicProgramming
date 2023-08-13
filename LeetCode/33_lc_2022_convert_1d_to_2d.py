from typing import List


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
