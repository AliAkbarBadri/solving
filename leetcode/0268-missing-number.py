# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missed = len(nums) * (len(nums) + 1) // 2 - sum(nums)
        nums.clear()
        return missed

    def missingNumber2(self, nums: List[int]) -> int:
        hashmap = set(nums)
        for number in range(len(nums) + 1):
            if not number in hashmap:
                return number

    def missingNumber3(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for idx in range(len(nums)):
            if nums[idx] != idx:
                return idx
        return len(nums)


sol = Solution()
assert sol.missingNumber([3, 0, 1]) == 2
assert sol.missingNumber([0, 1]) == 2
assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
