# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for value in nums:
            if value in hashset:
                return True
            hashset.add(value)
        return False
    

sol = Solution()
assert (sol.containsDuplicate(nums = [1,2,3,1]) == True)
assert (sol.containsDuplicate(nums = [1,2,3,4]) == False)
assert (sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]) == True)