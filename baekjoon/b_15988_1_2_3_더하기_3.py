t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if i <= 3:
            dp[i] = 1
        dp[i] += dp[i-1]
        if i - 3 >= 0:
            dp[i] += dp[i-3]
        if i - 2 >= 0:
            dp[i] += dp[i-2]
        dp[i] = dp[i] % 1000000009
    print(dp[-1])