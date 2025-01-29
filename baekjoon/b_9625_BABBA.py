n = int(input())
dp = [[0, 0] for _ in range(2)]
dp[0] = [0, 1]
dp[1] = [1, 1]
if n >= 2:
    for i in range(2, n):
        dp.append([dp[i-1][1], dp[i-1][0] + dp[i-1][1]])
print(dp[n-1][0], dp[n-1][1])