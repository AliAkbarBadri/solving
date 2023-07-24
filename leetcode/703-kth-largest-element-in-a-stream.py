# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap)>k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]        

kth_largest = KthLargest(3, [4, 5, 8, 2])
assert kth_largest.add(3) == 4
assert kth_largest.add(5) == 5
assert kth_largest.add(10) == 5
assert kth_largest.add(9) == 8
assert kth_largest.add(4) == 8