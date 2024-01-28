# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(first_idx: int, path: List, sum: int):
            if sum == target:
                results.append(path)
                return
            elif sum > target:
                return
            for i in range(first_idx, len(candidates)):
                backtrack(i, path+[candidates[i]], sum+candidates[i])

        results = []
        backtrack(0, [], 0)
        return results


sol = Solution()
print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(sol.combinationSum(candidates=[2, 3, 5], target=8))
print(sol.combinationSum(candidates=[2], target=1))
