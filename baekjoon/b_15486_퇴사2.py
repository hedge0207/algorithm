import sys


input = sys.stdin.readline
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)
max_ = 0
for i in range(N):
    if max_ < dp[i]:
        max_ = dp[i]

    t, p = table[i]
    if t + i > N:
        continue

    if dp[t+i] < max_ + p:
        dp[t+i] = max_ + p

print(max(dp))