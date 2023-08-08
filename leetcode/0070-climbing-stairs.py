# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


sol = Solution()
assert sol.climbStairs(n=2) == 2
assert sol.climbStairs(n=3) == 3
assert sol.climbStairs(n=4) == 5
