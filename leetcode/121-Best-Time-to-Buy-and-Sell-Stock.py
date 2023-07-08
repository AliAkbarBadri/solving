# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            - if i is a good buy so for j>i, a[j]>a[i], a[j] is not good enough, so do not try j.
            - we keep the best, so if you move i to a new index because for k>i, a[k]<a[i], don't worry. best
            wont be lost and we just try to find new best with a less buy(a[k]) and if we can not find it, we
            just have the best.
        """
        buy = prices[0]
        best = 0
        for sell in prices[1:]:
            if buy > sell:
                buy = sell
                # sell-oldbuy<0 so do not max
                continue
            best = max(best, sell - buy)
        return best


sol = Solution()
assert (sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
assert (sol.maxProfit([7, 6, 4, 3, 1]) == 0)
