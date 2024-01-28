from typing import List


class Solution:
    def __init__(self) -> None:
        self.hashmap = {}
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, value in enumerate(nums):
            idx2 = self.hashmap.get(-target - value, -1)
            if idx2 != -1:
                return [idx2, idx]
            self.hashmap[value] = idx
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for idx, target in enumerate(nums):
            result.append([target]+self.twoSum(nums[:idx]+nums[idx+1:], target))
        return result


sol = Solution()
assert sorted(sol.threeSum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])
assert sorted(sol.threeSum([0, 1, 1])) == sorted([])
assert sorted(sol.threeSum([0, 0, 0])) == sorted([0, 0, 0])
