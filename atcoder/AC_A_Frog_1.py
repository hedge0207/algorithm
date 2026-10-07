n = int(input())
stones = list(map(int, input().split()))
dp = [float("inf")] * n
dp[0], dp[1] = 0, abs(stones[0]-stones[1])

for i in range(2, n):
    dp[i] = min(dp[i-2] + abs(stones[i] - stones[i-2]), dp[i-1] + abs(stones[i] - stones[i-1]))
print(dp[-1])