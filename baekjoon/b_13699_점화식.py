# 재귀
def f(n: int) -> int:
    if dp[n] != 0:
        return dp[n]
    ans = 0
    for i in range(n):
        ans += f(i) * f(n-(i + 1))
    dp[n] = ans
    return ans

n = int(input())
dp = [0] * (n+1)
dp[0] = 1
print(f(n))


# 반복
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - 1 - j]
print(dp[n])

