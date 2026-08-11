n = int(input())
nums = list(map(int, input().split()))

idx_per_num = {}
for i, num in enumerate(nums):
    idx_per_num[num] = i

ans = 1
for i in range(n-1, -1, -1):
    num = nums[i]
    if num != 1:
        if idx_per_num[num-1] > i:
            ans += 1
print(ans)