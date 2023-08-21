# https://leetcode.com/problems/coin-change/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return 0


sol = Solution()
assert sol.coinChange(coins=[1, 2, 5], amount=11) == 3
assert sol.coinChange(coins=[2], amount=3) == -1
assert sol.coinChange(coins=[1], amount=0) == 0
