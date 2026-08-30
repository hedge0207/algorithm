class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans = []
        for i in range(1, 10):
            sequential_digit = i
            for j in range(i+1, 10):
                sequential_digit = sequential_digit * 10 + j
                if low <= sequential_digit <= high:
                    ans.append(sequential_digit)
        return sorted(ans)