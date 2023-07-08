# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

sol = Solution()
assert (sol.isAnagram(s="anagram", t="nagaram") == True)
assert (sol.isAnagram(s="rat", t="car") == False)
assert (sol.isAnagram(s="aa", t="a") == False)
