class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        ans = n
        while 1:
            product = 1
            for digit in str(ans):
                product *= int(digit)
            if product % t == 0:
                return ans
            ans += 1