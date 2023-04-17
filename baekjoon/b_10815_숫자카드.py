import sys


def binary_search(num):
    st, ed = 0, N - 1
    while st <= ed:
        mid = (st + ed + 1) // 2

        if cards[mid] == num:
            return 1
        elif cards[mid] > num:
            ed = mid - 1
        else:
            st = mid + 1

    return 0


input = sys.stdin.readline
N = int(input())
cards = sorted(list(map(int, input().split())))
_ = input()
for num in list(map(int, input().split())):
    print(binary_search(num), end=" ")