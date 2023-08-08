# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight2(self, n: int) -> int:
        counter = 0
        while n != 0:
            if n % 2:
                counter += 1
            n //= 2
        return counter

    def hammingWeight3(self, n: int) -> int:
        counter = 0
        while n:
            if n & 1:
                counter += 1
            n >>= 1
        return counter


sol = Solution()
assert sol.hammingWeight3(11) == 3
assert sol.hammingWeight3(128) == 1
assert sol.hammingWeight3(4294967293) == 31
