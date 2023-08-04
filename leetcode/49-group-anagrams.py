# https://leetcode.com/problems/group-anagrams/

from collections import Counter, defaultdict
from functools import reduce
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = defaultdict(list)
        for word in strs:
            char_count_list = 26 * [0]
            for char in word:
                char_count_list[ord(char) - 97] += 1
            words_dict[tuple(char_count_list)].append(word)
        return list(words_dict.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = defaultdict(list)
        for word in strs:
            words_dict["".join(sorted(word))].append(word)
        return list(words_dict.values())


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
assert (
    sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]).sort()
    == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ].sort()
)
assert sol.groupAnagrams(strs=[""]).sort() == [[""]].sort()
assert sol.groupAnagrams(strs=["a"]).sort() == [["a"]].sort()
