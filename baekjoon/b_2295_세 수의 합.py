import sys


def binary_search(target):
    st, ed = 0, num_sum_lst-1
    while st <= ed:
        mid = (st + ed) // 2
        if sum_lst[mid] == target:
            return True
        elif sum_lst[mid] > target:
            ed = mid - 1
        else:
            st = mid + 1


input = sys.stdin.readline
N = int(input())
nums = sorted([int(input()) for _ in range(N)])

sum_lst = []
for i in range(N):
    for j in range(i, N):
        sum_lst.append(nums[i] + nums[j])
sum_lst.sort()
result = 0
num_sum_lst = len(sum_lst)
for i in range(N - 1, -1, -1):
    for j in range(i+1):
        is_exist = binary_search(nums[i] - nums[j])
        if is_exist and nums[i] > result:
            result = nums[i]

print(result)
