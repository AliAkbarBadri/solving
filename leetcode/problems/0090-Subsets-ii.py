# https://leetcode.com/problems/subsets-ii

from typing import List, Set, Tuple


class Solution:
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int], path: List[int]):
            if path in results:
                return
            else:
                results.append(set(path))
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
        results = [[]]
        backtrack(nums, [])
        results = [list(item) for item in results]
        return results

    def subsetsWithDup3(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx: int, path: List):
            if idx == len(nums):
                return
            for j in range(idx, len(nums)):
                path.append(nums[j])
                if not path[:] in results:
                    results.append(path[:])
                backtrack(j+1, path)
                path.pop()
        nums = sorted(nums)
        results = [[]]
        backtrack(0, [])
        return results

    def subsetsWithDup4(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int], i: int, curr: List[int], ans: Set[Tuple[int]]):
            if i == len(nums):
                ans.add(tuple(curr[:]))
                return
            curr.append(nums[i])
            # instead of for loop; all the same
            backtrack(nums, i + 1, curr, ans)
            curr.pop()
            backtrack(nums, i + 1, curr, ans)

        nums.sort()
        curr = []
        ans = set()
        backtrack(nums, 0, curr, ans)
        return ans

    def subsetsWithDup4(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx: int, path: List):
            if idx == len(nums):
                return
            for j in range(idx, len(nums)):
                path.append(nums[j])
                results.add(tuple(path[:]))
                backtrack(j+1, path)
                path.pop()
        nums = sorted(nums)
        results = {()}
        backtrack(0, [])
        return results


sol = Solution()
print(sol.subsetsWithDup(nums=[2, 1, 2]))
assert sorted(sol.subsetsWithDup([0])) == sorted([[], [0]])
assert sorted(sol.subsetsWithDup(nums=[1, 2, 2])) == sorted(
    [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])

assert sorted(sol.subsetsWithDup(nums=[2, 1, 2])) == sorted(
    [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
