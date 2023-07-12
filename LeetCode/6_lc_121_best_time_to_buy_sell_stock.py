from typing import List
"""
- Easy -
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

given an array prices where prices[i] is the price of a given stock on the ith day. 
Return the maximum profit you can achieve from this transaction


Solution    -   73.8% in Runtime
            -   55.2% in Memory
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The solution uses a two pointer approach, where the first pointer is moved to last if last is lesser than first
        """
        maxim = 0
        first = 0
        last = 1
        prices_len = len(prices)
        while last < prices_len :
            if prices[first] < prices[last]:
                maxim = max(prices[last] - prices[first], maxim)
            else:
                first = last
            last +=1
        return maxim


print(Solution().maxProfit([9, 0, 1, 5, 3, 6, 4]))
