n = int(input())
nums = list(map(int, input().split()))
prefix_sum = [0] * n
prefix_sum[0] = nums[0]
ans = nums[0]
for i in range(1, n):
    prefix_sum[i] = max(nums[i], nums[i] + prefix_sum[i-1])
    ans = max(ans, prefix_sum[i])
print(ans)