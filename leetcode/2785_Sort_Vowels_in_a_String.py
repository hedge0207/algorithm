class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowels_in_s = []
        for i in range(len(s)):
            if s[i] in VOWELS:
                vowels_in_s.append(s[i])
        vowels_in_s.sort()
        ans = ""
        j = 0
        for i in range(len(s)):
            if s[i] in VOWELS:
                ans += vowels_in_s[j]
                j += 1
            else:
                ans += s[i]
        return ans