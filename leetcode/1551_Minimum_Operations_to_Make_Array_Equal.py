class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        median = (n*2+1) // 2
        for i in range(1, median, 2):
            ans += median - i
        return ans


    def best_practice(self, n: int) -> int:
        return (n // 2) * (n - n // 2)