import sys


# Python의 set 활용
# input = sys.stdin.readline
# N, M = map(int, input().split())
# set_a = set(map(int, input().split()))
# set_b = set(map(int, input().split()))
#
# ans = sorted(set_a.difference(set_b))
# print(len(ans))
# for num in ans:
#     print(num, end=" ")


# 이진 탐색 활용
def binary_search(target):
    st, ed = 0, M - 1
    while st <= ed:
        mid = (st + ed + 1) // 2

        if set_b[mid] == target:
            return 1
        elif set_b[mid] > target:
            ed = mid - 1
        else:
            st = mid + 1
    return 0

input = sys.stdin.readline
N, M = map(int, input().split())
set_a = sorted(list(map(int, input().split())))
set_b = sorted(list(map(int, input().split())))

subtraction = []
for num in set_a:
    if not binary_search(num):
        subtraction.append(num)

print(len(subtraction))
for num in subtraction:
    print(num, end=" ")