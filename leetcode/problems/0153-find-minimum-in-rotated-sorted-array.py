# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    @staticmethod
    def findMin(nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[left] <= nums[mid]:
                if nums[right] < nums[mid]:
                    left = mid + 1
                else:
                    return nums[left]
            elif nums[left] > nums[mid] and nums[mid] < nums[right]:
                right = mid

    @staticmethod
    def findMin2(nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = float("inf")

        while start < end:
            mid = (start + end) // 2
            curr_min = min(curr_min, nums[mid])
            # right has the min
            if nums[mid] > nums[end]:
                start = mid + 1
            # left has the  min
            else:
                end = mid - 1

        return min(curr_min, nums[start])


sol = Solution()
assert sol.findMin([3, 1, 2]) == 1
assert sol.findMin(nums=[3, 4, 5, 1, 2]) == 1
assert sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2]) == 0
assert sol.findMin(nums=[11, 13, 15, 17]) == 11
