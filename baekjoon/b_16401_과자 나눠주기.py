import sys


def parametric_search():
    st, ed = 1, candy[-1]
    valid_length = 0
    while st <= ed:
        mid = (st + ed + 1) // 2

        cnt = 0
        for length_candy in candy[::-1]:
            share = length_candy // mid
            if share == 0:
                break
            cnt += share

        if cnt >= M:
            valid_length = mid
            st = mid + 1
        else:
            ed = mid - 1

    return valid_length

input = sys.stdin.readline
M, N = map(int, input().split())
candy = sorted(list(map(int, input().split())))
print(parametric_search())