class Solution:
    def minOperations(self, s: str) -> int:
        alternating_binary = ""
        bit = "0"
        for i in range(len(s)):
            alternating_binary += bit
            if bit == "1":
                bit = "0"
            else:
                bit = "1"

        ans = 0
        for i in range(len(s)):
            if s[i] != alternating_binary[i]:
                ans += 1

        alternating_binary = ""
        bit = "1"
        for i in range(len(s)):
            alternating_binary += bit
            if bit == "1":
                bit = "0"
            else:
                bit = "1"

        cnt = 0
        for i in range(len(s)):
            if s[i] != alternating_binary[i]:
                cnt += 1

        return min(ans, cnt)