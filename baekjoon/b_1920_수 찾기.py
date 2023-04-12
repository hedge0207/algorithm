import sys


def binary_search():
    st, ed = 0, arr_length
    while st <= ed:
        mid = (st + ed) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            ed = mid - 1
        else:
            st = mid + 1

    return 0


input = sys.stdin.readline
_ = input()
arr = sorted(list(map(int, input().split())))
_ = input()
targets = list(map(int, input().split()))

arr_length = len(arr) - 1
for target in targets:
    print(binary_search())