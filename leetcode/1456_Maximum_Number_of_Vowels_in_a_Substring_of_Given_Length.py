class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        vowels = {"a", "e", "i", "o", "u"}
        num_vowels = 0
        st = 0
        for ed in range(len(s)):
            if s[ed] in vowels:
                num_vowels += 1
            if ed >= k:
                if s[st] in vowels:
                    num_vowels -= 1
                st += 1
            ans = max(ans, num_vowels)
        return ans