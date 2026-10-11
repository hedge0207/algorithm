n = int(input())
nums = list(map(int, input().split()))

ans = 0
for i in range(n-2):
    if nums[i] < nums[i+1] and nums[i+2] < nums[i+1]:
        ans += 1
print(ans)