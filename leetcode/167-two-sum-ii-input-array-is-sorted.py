# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            summation = numbers[left] + numbers[right]
            if target < summation:
                right -= 1
            elif target > summation:
                left += 1
            else:
                return [left + 1, right + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, value in enumerate(numbers):
            idx2 = hashmap.get(target - value, -1)
            if idx2 != -1:
                return [idx2 + 1, idx + 1]
            hashmap[value] = idx


sol = Solution()
assert sol.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
assert sol.twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
assert sol.twoSum(numbers=[-1, 0], target=-1) == [1, 2]
