# https://leetcode.com/problems/permutations

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int], path: List[int]):
            if len(nums) == 1:
                results.append(path+nums)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
        results = []
        backtrack(nums, [])
        return results


sol = Solution()
assert sorted(sol.permute(nums=[0, 1])) == sorted([[0, 1], [1, 0]])
assert sorted(sol.permute(nums=[1, 2, 3])) == sorted([[1, 2, 3], [1, 3, 2], [
    2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
assert sorted(sol.permute(nums=[1])) == sorted([[1]])
