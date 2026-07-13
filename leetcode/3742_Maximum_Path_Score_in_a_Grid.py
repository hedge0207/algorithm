class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        costs = [0, 1, 1]
        dp = [[[-1]*(k+1) for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0

        for i in range(n):
            for j in range(m):
                score = grid[i][j]
                cur_cost = costs[score]
                if i - 1 >= 0:
                    for cost in range(k-cur_cost+1):
                        if dp[i-1][j][cost] == -1:
                            continue
                        dp[i][j][cost + cur_cost] = max(dp[i-1][j][cost] + score, dp[i][j][cost+cur_cost])
                if j - 1 >= 0:
                    for cost in range(k-cur_cost+1):
                        if dp[i][j-1][cost] == -1:
                            continue
                        dp[i][j][cost + cur_cost] = max(dp[i][j-1][cost] + score, dp[i][j][cost + cur_cost])
        ans = -1
        for score in dp[-1][-1]:
            ans = max(ans, score)
        return ans