n = int(input())

dp = [0]*(n+1)
dp[0], dp[1] = 1, 1

def fibo(d):
    if dp[d]:
        return dp[d]
    dp[d] = fibo(d-1) + fibo(d-2)
    return dp[d]

fibo(n)
print(dp[-1]*2 + dp[-2]*2)

