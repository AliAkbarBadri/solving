# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, path: str) -> List[str]:
            if len(path) == 2*n:
                results.append(path)
                return
            if left < n:
                backtrack(left+1, right, path+"(")
            if right < left:
                backtrack(left, right+1, path+")")
            return
        results = []
        backtrack(0, 0, "")
        return results

    def generateParenthesis2(self, n: int) -> List[str]:
        def backtrack(stack, path: str) -> List[str]:
            if stack < 0 or stack > n or len(path) > 2*n:
                return
            if stack == 0 and len(path) == 2*n:
                results.append(path)
                return
            path += "("
            stack += 1
            backtrack(stack, path)
            path = path[:-1]
            path += ")"
            stack -= 2
            backtrack(stack, path)
        results = []
        backtrack(0, "")
        return results


solution = Solution()
assert solution.generateParenthesis(n=1) == ["()"]
assert sorted(solution.generateParenthesis(n=3)) == sorted(
    ["((()))", "(()())", "(())()", "()(())", "()()()"])
