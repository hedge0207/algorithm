n = int(input())

dp = [1]
for i in range(1, n+1):
    if i < 7:
        dp.append(sum([dp[j] for j in range(i)]))
    else:
        dp.append(sum([dp[-j] for j in range(1, 7)]) % (10**9+7))

print(dp[-1])
