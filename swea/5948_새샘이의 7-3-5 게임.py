import sys
sys.stdin = open("5948_input.txt", "r")


def f(k, s, c):
    if k == 3:
        sum_list.append(s)
    else:
        for i in range(len(num_l)):
            if visited[i] == 1:
                continue
            else:
                visited[i] = 1
                f(k + 1, s + num_l[i], i)
                visited[i] = 0


def partion(ml, st, ed):
    a = st
    b = st
    p = ed
    while a < p:
        if ml[a] <= ml[p]:
            ml[a], ml[b] = ml[b], ml[a]
            b += 1
        a += 1
    ml[b], ml[p] = ml[p], ml[b]
    p = b
    return p


def quick(ml, st, ed):
    if ed - st < 1:
        return
    p = partion(ml, st, ed)
    quick(ml, st, p - 1)
    quick(ml, p + 1, ed)


for tc in range(1, int(input()) + 1):
    num_l = list(map(int, input().split()))
    visited = [0] * 7
    sum_list = []
    f(0, 0, 0)

    quick(sum_list, 0, len(sum_list) - 1)

    print(sum_list)
    print(sum_list[-5])
