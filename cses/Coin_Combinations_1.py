import sys

input = sys.stdin.readline
MOD = (10**9+7)
n, x = map(int, input().split())
coins = sorted(list(map(int, input().split())))
dp = [0] * (x + 1)
dp[0] = 1
for i in range(min(coins), x+1):
    for coin in coins:
        if coin > i:
            break
        dp[i] += dp[i-coin]
        dp[i] %= MOD
print(dp[-1])