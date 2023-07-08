# https://leetcode.com/problems/valid-anagram/

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        if len(s) != len(t) or set(s) != set(t):
            return False
        for char_s, char_t in zip(s,t):
            hashmap_s[char_s] = hashmap_s.get(char_s,0)+1
            hashmap_t[char_t] = hashmap_t.get(char_t,0)+1
        return hashmap_s == hashmap_t


sol = Solution()
assert (sol.isAnagram(s="anagram", t="nagaram") == True)
assert (sol.isAnagram(s="rat", t="car") == False)
assert (sol.isAnagram(s="aa", t="a") == False)
