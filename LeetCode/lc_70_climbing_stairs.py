"""
https://leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Solution:
Solution    -   Timeout exceeded

"""

class Solution:
    total_solutions = 0
    def climb(self, n: int):
        if n == 1:
            self.total_solutions += 1
        elif n == 2:
            self.total_solutions += 2
        else:
            self.climb(n-1)
            self.climb(n-2)

    def climbStairs(self, n: int) -> int:
        self.climb(n)
        return self.total_solutions

    def neetcode(self, n: int) -> int:
        first = 1
        second = 1
        for i in range(1, n):
            temp = first
            first = first + second
            second = temp
        return first



print(Solution().neetcode(50))

