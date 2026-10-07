import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stones = list(map(int, input().split()))
dp = [float("inf")] * n
dp[0] = 0

for i in range(n):
    for j in range(1, k+1):
        if i - j >= 0:
            dp[i] = min(dp[i-j] + abs(stones[i] - stones[i-j]), dp[i])
print(dp[-1])