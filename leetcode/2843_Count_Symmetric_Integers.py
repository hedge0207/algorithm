class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high+1):
            num = str(num)
            n = len(str(num))
            if n % 2 == 1:
                continue

            digits = []
            for char in num:
                digits.append(char)
            digits = list(map(int ,digits))
            if sum(digits[:n//2]) == sum(digits[n//2:]):
                ans += 1

        return ans