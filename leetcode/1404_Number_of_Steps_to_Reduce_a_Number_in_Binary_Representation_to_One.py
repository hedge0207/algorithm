class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        while len(s) > 1:
            if s[-1] == "0":
                s = s[:-1]
            else:
                decimal_number = int(s, 2)
                s = bin(decimal_number + 1)[2:]
            ans += 1
        return ans