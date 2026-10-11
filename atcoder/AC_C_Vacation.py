n = int(input())
points_per_day = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = points_per_day[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + points_per_day[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + points_per_day[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + points_per_day[i][2]

print(max(dp[-1]))