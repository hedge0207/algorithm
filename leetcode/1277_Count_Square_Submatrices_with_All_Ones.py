# 못 푼 문제
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        n, m  = len(matrix), len(matrix[0])
        dp = [[0] * (m+1) for _ in range(n+1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    ans += dp[i+1][j+1]
        return ans



