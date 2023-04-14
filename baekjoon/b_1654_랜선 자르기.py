import sys


def upper_bound():
    result = 0
    st, ed = 0, max_value
    while st < ed:
        mid = (st + ed + 1) // 2

        num_cables = 0
        for length_cable in cables:
            num_cables += length_cable // mid

        if num_cables < N:
            ed = mid - 1
        else:
            result = mid
            st = mid

    return result


input = sys.stdin.readline
K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
max_value = max(cables)
print(upper_bound())