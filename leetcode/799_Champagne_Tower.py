class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * i for i in range(1, 101)]
        dp[0][0] = poured
        for i in range(1, 100):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = (dp[i - 1][0] - 1) / 2 if dp[i-1][0] >= 1 else 0
                elif j == len(dp[i]) - 1:
                    dp[i][j] = (dp[i - 1][-1] - 1) / 2 if dp[i-1][-1] >= 1 else 0
                else:
                    dp[i][j] += (dp[i - 1][j - 1] - 1) / 2 if dp[i - 1][j-1] >= 1 else 0
                    dp[i][j] += (dp[i - 1][j] - 1) / 2 if dp[i - 1][j] >= 1 else 0
            if i == query_row:
                break

        if dp[query_row][query_glass] > 1:
            return 1.000
        elif dp[query_row][query_glass] < 0:
            return 0.000
        else:
            return dp[query_row][query_glass]