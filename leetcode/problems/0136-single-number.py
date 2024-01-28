# https://leetcode.com/problems/single-number/


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_list = sum(nums)
        sum_set = sum(set(nums))
        nums.clear()
        return 2 * sum_set - sum_list

    def singleNumber2(self, nums: List[int]) -> int:
        # a ^ a = 0
        # a ^ b ^ a = b
        res = 0
        for n in nums:
            res = n ^ res
        nums.clear()
        return res


sol = Solution()
# assert (sol.singleNumber([2, 2, 1]) == 1)
assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
# assert (sol.singleNumber([1]) == 1)
