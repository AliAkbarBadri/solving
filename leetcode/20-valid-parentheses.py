# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if not char in mapper:
                stack.append(char)
            elif len(stack)<=0 or mapper[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return len(stack)<=0


sol = Solution()
assert (sol.isValid(s="()") == True)
assert (sol.isValid(s="()[]{}") == True)
assert (sol.isValid(s="(]") == False)
assert (sol.isValid(s="([)]") == False)
assert (sol.isValid(s="[") == False)
assert (sol.isValid(s="]") == False)
