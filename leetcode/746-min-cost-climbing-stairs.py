# https://leetcode.com/problems/min-cost-climbing-stairs/description/


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last_last = cost[-1]
        last = cost[-2]
        for i in range(len(cost)-3, -1, -1):
            curr = min(last, last_last) + cost[i]
            last_last, last = last, curr
        return min(last, last_last)

sol = Solution()
assert sol.minCostClimbingStairs([10, 15, 20]) == 15
assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
