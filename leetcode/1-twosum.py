# https://leetcode.com/problems/two-sum/


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, value in enumerate(nums):
            hashmap[value] = idx
        for idx, value in enumerate(nums):
            idx2 = hashmap.get(target - value)
            if idx2 and idx2 != idx:
                return [idx, idx2]


sol = Solution()
assert (sol.twoSum([2, 7, 11, 15], 9) == [0, 1])
assert (sol.twoSum(nums=[3, 2, 4], target=6) == [1, 2])
