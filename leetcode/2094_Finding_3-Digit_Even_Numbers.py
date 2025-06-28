class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        ans = set()
        n = len(digits)
        for i in range(n):
            if digits[i] % 2:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if i == k or j == k:
                        continue
                    if digits[k] == 0:
                        continue
                    num = digits[k] * 100 + digits[j] * 10 + digits[i]
                    ans.add(num)
        return sorted(list(ans))