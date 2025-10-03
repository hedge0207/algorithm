n = int(input())
prices = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j-1] + prices[j])
print(dp[-1])