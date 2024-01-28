from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int], path: List):
            if set(path) in results:
                return
            else:
                results.append(set(path))
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
            return
        results = []
        backtrack(nums, [])
        results = [list(item) for item in results]
        return results

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, path):
            if idx == len(nums):
                return
            for j in range(idx, len(nums)):
                path.append(nums[j])
                results.append(path[:])
                backtrack(j+1, path)
                path.pop()
        results = [[]]
        backtrack(0, [])
        return results

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for i in range(len(nums)):
            for j in range(len(results)):
                temp = results[j].copy()
                temp.append(nums[i])
                results.append(temp)
        return results


sol = Solution()
assert sorted(sol.subsets(nums=[0])) == sorted([[], [0]])
assert sorted(sol.subsets(nums=[1, 2, 3])) == sorted(
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
