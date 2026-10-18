n, x = map(int, input().split())
ranges = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (x+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    a, b = ranges[i-1]
    for j in range(x+1):
        if dp[i-1][j]:
            if j + a <= x:
                dp[i][j+a] = 1
            if j + b <= x:
                dp[i][j+b] = 1

print("Yes" if dp[-1][-1] else "No")