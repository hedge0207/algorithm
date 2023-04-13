import sys


def binary_search(arr, num):
    st, ed = 0, len(arr) - 1
    while st <= ed:
        mid = (st + ed) // 2
        if arr[mid] > num:
            ed = mid - 1
        elif arr[mid] < num:
            st = mid + 1
        else:
            return mid

    return -1


def compress_coordinate():
    sorted_lst = sorted(coordinates)
    unique_lst = [sorted_lst[0]]
    for num in sorted_lst:
        if num != unique_lst[-1]:
            unique_lst.append(num)

    result = []
    for num in coordinates:
        result.append(binary_search(unique_lst, num))

    for num in result:
        print(num, end=" ")


input = sys.stdin.readline
N = int(input())
coordinates = list(map(int, input().split()))
compress_coordinate()
