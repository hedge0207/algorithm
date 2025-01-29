n = int(input())
stairs = [int(input()) for _ in range(n)]

if n == 0:
    print(0)
elif n == 1:
    print(stairs[0])
else:
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, n):
        dp[i] = max(stairs[i] + dp[i-2], dp[i-3] + stairs[i-1] + stairs[i])
    print(dp[-1])