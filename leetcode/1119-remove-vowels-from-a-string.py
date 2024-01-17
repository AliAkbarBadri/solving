
class Solution:
    def remove_vowels(self, text: str) -> str:
        output = ""
        for char in text:
            if not char.lower() in "aeiou":
                output += char
        return output


sol = Solution()
assert sol.remove_vowels(text="anagram") == "ngrm"
assert sol.remove_vowels(text="aeiou") == ""
