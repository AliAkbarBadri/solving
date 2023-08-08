# https://leetcode.com/problems/valid-palindrome/

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = re.sub(r'[\W_]', '', s).lower()
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


sol = Solution()
assert sol.isPalindrome(s="A man, a plan, a canal: Panama") == True
assert sol.isPalindrome(s="race a car") == False
assert sol.isPalindrome(s=" ") == True
