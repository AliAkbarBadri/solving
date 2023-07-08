# https://leetcode.com/problems/valid-anagram/

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t) or set(s) != set(t):
            return False
        for char_s, char_t in zip(s,t):
            hashmap[char_s] = hashmap.get(char_s,0)+1
            hashmap[char_t] = hashmap.get(char_t,0)-1
        return not any(hashmap.values())


sol = Solution()
assert (sol.isAnagram(s="anagram", t="nagaram") == True)
assert (sol.isAnagram(s="rat", t="car") == False)
assert (sol.isAnagram(s="aa", t="a") == False)
