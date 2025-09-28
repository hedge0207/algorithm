class Solution:
    def maxScore(self, s: str) -> int:
        num_one = 0
        for char in s:
            if char == "1":
                num_one += 1

        ans = 0
        num_zero = 0
        for i in range(len(s)-1):
            if s[i] == "1":
                num_one -= 1
            else:
                num_zero += 1
            ans = max(ans, num_one + num_zero)
        return ans




















s = Solution()
print(s.maxScore("011101"))
print(s.maxScore("00111"))
print(s.maxScore("1111"))
print(s.maxScore("00"))
print(s.maxScore("11100"))



