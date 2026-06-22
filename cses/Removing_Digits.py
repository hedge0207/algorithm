import sys
input = sys.stdin.readline


n = int(input())
dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for digit in str(i):
        d = int(digit)
        dp[i] = min(dp[i], dp[i - d] + 1)

print(dp[n])