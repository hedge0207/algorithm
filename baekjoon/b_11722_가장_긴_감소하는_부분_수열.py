n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i+1, n):
        if nums[j] < nums[i]:
            dp[j] = max(dp[j], dp[i]+1)
print(max(dp))




















"""
5
5 2 6 9 7

5
9 2 5 2 10

3
4 1 2

6
5 3 4 2 1 0

5
5 1 8 7 6

3
4 6 3
"""
