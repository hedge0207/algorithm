n = int(input())
wines = list(map(int, [input() for _ in range(n)]))

if n < 3:
    print(sum(wines))
else:
    dp = [0 for _ in range(n)]
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(dp[1], wines[0]+wines[2], wines[1]+wines[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i]+wines[i-1])

    print(dp[-1])
