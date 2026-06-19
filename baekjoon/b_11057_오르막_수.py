n = int(input())
dp = [[0]*10 for _ in range(n)]
dp[0] = [1 for i in range(10)]
for i in range(1, n):
    dp[i][0] = sum(dp[i-1])
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1]-dp[i-1][j-1]
print(sum(dp[n-1]) % (10**4+7))

# best_practice
N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i-1][k]
print(sum(dp[N]) % 10007)