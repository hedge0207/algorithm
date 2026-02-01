class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        num_zero = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0" and i > 0 and s[i-1] == "1":
                num_zero += 1
            if s[i] == "1":
                ans += num_zero
        return ans