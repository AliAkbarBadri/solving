# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Runtime 58 ms, Memory 16.8 MB
        return Counter(s) == Counter(t)
        #Runtime 72 ms, Memory 17.5 MB
        #return sorted(s) == sorted(t)

sol = Solution()
assert (sol.isAnagram(s="anagram", t="nagaram") == True)
assert (sol.isAnagram(s="rat", t="car") == False)
assert (sol.isAnagram(s="aa", t="a") == False)
