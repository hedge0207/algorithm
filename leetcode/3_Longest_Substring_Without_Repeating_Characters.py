class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub = ''
        for ed in range(len(s)):
            char = s[ed]
            if char in sub:
                max_len = max(max_len, len(sub))
                while char in sub:
                    sub = sub[1:ed+1]
            sub += char
        max_len = max(max_len, len(sub))

        return max_len


