class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[0]*(i+1) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
            for j in range(1, len(triangle[i])-1):
                dp[i][j] = min(dp[i-1][j]+triangle[i][j], dp[i-1][j-1]+triangle[i][j])

        return min(dp[-1])


# best practice
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = min(dp[i], dp[i + 1]) + n
        return dp[0]
