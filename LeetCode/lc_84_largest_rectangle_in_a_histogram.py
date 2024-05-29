from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Iterative approach with a bit of optimization to avoid repetition
        Solution:
            Time limit exceeded
        """
        max_rect = 0
        i = 0
        delta = 0
        while i < len(heights):
            k = i -1
            while True:
                if k >= 0 and heights[k] >= heights[i]:
                    k -= 1
                else:
                    break
            l = i+1
            while True:
                if l < len(heights) and heights[l] >= heights[i]:
                    # Moving i pointer to avoid repeating operation on equal adjacent heights
                    delta = delta + heights[l] - heights[i]
                    if delta == 0:
                        i = l
                    l += 1
                else:
                    break
            result = (l - k-1) * heights[i]
            max_rect = max(max_rect, result)
            i+= 1

        return max_rect

    def largestRectangleArea2(self, heights: List[int]) -> int:
        """
        Solution from neetcode

        Runtime: 89%
        Memory: 66%
        """

        rect_stack = []
        max_height = 0
        i = 0
        while i < len(heights):
            if not rect_stack or rect_stack[-1][1] < heights[i]:
                rect_stack.append((i, heights[i]))
            else:
                last_i = 0
                while rect_stack and rect_stack[-1][1] >= heights[i]:
                    last_i, last_height = rect_stack.pop()
                    if last_height != heights[i]:
                        max_height = max(max_height, last_height * (i - last_i))
                rect_stack.append((last_i, heights[i]))
            i += 1
        while rect_stack:
            last_i, last_height = rect_stack.pop()
            max_height = max(max_height, last_height * (i - last_i))

        return max_height






print(Solution().largestRectangleArea2([1,2,2]))
