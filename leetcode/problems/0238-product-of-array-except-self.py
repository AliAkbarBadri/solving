from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = len(nums) * [1]
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        post = 1
        for i in range(len(nums) - 2, -1, -1):
            post *= nums[i + 1]
            # output = pre*post
            output[i] *= post
        return output


sol = Solution()
assert sol.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
assert sol.productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
