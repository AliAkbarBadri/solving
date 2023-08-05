# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in s[i:j]:
                    break
                max_len = max(max_len, len(s[i : j + 1]))
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        not_breaked = True
        while i < len(s):
            if not_breaked:
                j = i
            while j < len(s):
                if s[j] in s[i:j]:
                    not_breaked = False
                    break
                max_len = max(max_len, len(s[i : j + 1]))
                j += 1
            i += 1
        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
assert sol.lengthOfLongestSubstring(s="abcabcbb") == 3
assert sol.lengthOfLongestSubstring(s="bbbbb") == 1
assert sol.lengthOfLongestSubstring(s="pwwkew") == 3
