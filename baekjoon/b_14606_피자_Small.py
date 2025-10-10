def get_pressure(n):
    if n == 1:
        return 0

    if dp[n]:
        return dp[n]

    a, b = n // 2, n // 2
    if n % 2:
        a += 1
    dp[n] = a * b + get_pressure(a) + get_pressure(b)
    return dp[n]

N = int(input())
dp = [0]*(N+1)
if N > 1:
    dp[2] = 1
get_pressure(N)
print(dp[-1])