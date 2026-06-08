n = int(input())
for _ in range(n):
    month = int(input())
    if month < 2:
        print(1)
        continue
    dp = [0] * (month+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, month+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[-1])