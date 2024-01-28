# https://leetcode.com/problems/last-stone-weight/


import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        stones.clear()
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(x - y))
        heap.append(0)
        return -heap[0]


sol = Solution()
assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
assert sol.lastStoneWeight([1]) == 1
