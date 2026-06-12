import sys


input = sys.stdin.readline
n = int(input())
for _ in range(n):
    shells = list(map(int, input().split()))
    dp = [0] * (len(shells) + 1)
    for i in range(4):
        dp[i] = i

    for i in range(len(shells)):
        if i >= 4:
            dp[i] = dp[i-4] + dp[i-3] + dp[i-2] + dp[i-1]
        if shells[i] != dp[i]:
            print("SNAIL")
            break
    else:
        print("NAUTILUS")



