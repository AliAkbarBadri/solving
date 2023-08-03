# https://leetcode.com/problems/two-sum/


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, value in enumerate(nums):
            idx2 = hashmap.get(target - value, -1)
            if idx2 != -1:
                return [idx2, idx]
            hashmap[value] = idx


sol = Solution()
assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert sol.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
