# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > best:
                    best = prices[j] - prices[i]
        return best
    
sol = Solution()
assert (sol.maxProfit([7,1,5,3,6,4]) == 5)
assert (sol.maxProfit([7,6,4,3,1]) == 0)

