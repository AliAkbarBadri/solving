# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


sol = Solution()
assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
assert sol.plusOne([9, 8, 9]) == [9, 9, 0]
assert sol.plusOne([9]) == [1, 0]
assert sol.plusOne([0]) == [1]
