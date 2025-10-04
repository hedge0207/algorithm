H, Y = map(int, input().split())
dp = [H] * (Y+1)

rates = {1:0.05, 3: 0.2, 5: 0.35}

for i in range(1, Y+1):
    max_ = 0
    for j in [1, 3, 5]:
        if i >= j:
            max_ = max(max_, int(dp[i-j]+dp[i-j]*rates[j]))
    dp[i] = max_

print(dp[-1])