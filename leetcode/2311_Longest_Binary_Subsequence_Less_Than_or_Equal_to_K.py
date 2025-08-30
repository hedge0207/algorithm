class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        num = 0
        position = 0
        ans = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                digit = 2**position
                if num + digit > k:
                    continue
                num += digit
            position += 1
            ans = s[i] + ans
        return len(ans)