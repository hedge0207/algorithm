import sys


input = sys.stdin.readline
N = int(input())
nums = sorted([int(input()) for _ in range(N)])
count = {}
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

frequent_nums = []
max_val = max(count.values())
for num, cnt in count.items():
    if cnt == max_val:
        frequent_nums.append(num)
frequent_nums.sort()

print(round(sum(nums) / N))
print(nums[N // 2])
if len(frequent_nums) >= 2:
    print(frequent_nums[1])
else:
    print(frequent_nums[0])
print(nums[-1] - nums[0])