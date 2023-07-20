class Solution:

    def fibo(self, n):
        if n <= 1:
            return n

        if self.memo[n]:
            return self.memo[n]

        self.memo[n] = self.fibo(n - 2) + self.fibo(n - 1)
        return self.memo[n]

    def climbStairs(self, n: int) -> int:
        self.memo = [0] * (n + 2)
        return self.fibo(n + 1)