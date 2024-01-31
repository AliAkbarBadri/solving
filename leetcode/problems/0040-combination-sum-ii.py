# https://leetcode.com/problems/combination-sum-ii/

from typing import List, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx: int, path: List[int], sum: int):
            if sum == target:
                results.append(path)
                return
            if sum > target or target < 0:
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1, path+[candidates[i]], sum+candidates[i])
        results = []
        candidates.sort()
        backtrack(0, [], 0)
        return results


solution = Solution()
# print(len(solution.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 30)[0]))

assert sorted(solution.combinationSum2(
    [2, 5, 2, 1, 2], 5)) == sorted([[1, 2, 2], [5]])
assert sorted(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == sorted(
    [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
