# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:

    # def hammingWeight(self, n: int) -> int:
    #     counter = 0
    #     while n:
    #         if n & 1:
    #             counter += 1
    #         n >>= 1
    #     return counter
    
    # def countBits(self, n: int) -> List[int]:
    #     return map(self.hammingWeight, range(0,n+1))
    def countBits(self, n: int) -> List[str]:
        dp = [0]*(n+1)
        for number in range(n+1):
            dp[number] = dp[number//2] + (number%2)
            # dp[number] = dp[number>>1] + (number&1)
        return dp
sol = Solution()
assert(sol.countBits(2)==[0,1,1])
assert(sol.countBits(5)==[0,1,1,2,1,2])
