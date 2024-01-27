# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits2char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        results = []

        def backtrack(idx, path):
            if len(path) == len(digits):
                results.append(path)
                return
            for char in digits2char[digits[idx]]:
                backtrack(idx+1, path+char)
        backtrack(0, "")
        return results


sol = Solution()
print(sol.letterCombinations(digits=""))
