# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "#035b")[:2:-1], 2)

    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
sol = Solution()
assert(sol.reverseBits(43261596)==964176192)
assert(sol.reverseBits(4294967293)==3221225471)