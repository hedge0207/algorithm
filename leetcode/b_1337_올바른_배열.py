import sys

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
max_adj_num = 0
for i in range(len(nums)):
    sub_set = nums[i:i+5]
    adj_num = 0
    for j in range(5):
        if nums[i] + j in sub_set:
            adj_num += 1
    max_adj_num = max(max_adj_num, adj_num)

if max_adj_num > 5:
    print(0)
else:
    print(5-max_adj_num)