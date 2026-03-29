n, k = map(int, input().split())
x, a, b, c = map(int, input().split())
nums = [x]
for i in range(n-1):
    nums.append((a*nums[-1]+b) % c)

sum_ = 0
for i in range(k):
    sum_ += nums[i]

ans = sum_
for i in range(k, n):
    sum_ += nums[i] - nums[i-k]
    ans ^= sum_
print(ans)