import sys
sys.stdin = open("5205_input.txt", 'r')


def partion(st, ed, ml):
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


def quick_sort(st, ed, ml):
    if ed - st < 1:
        return

    p = partion(st, ed, ml)

    quick_sort(st, p - 1, ml)
    quick_sort(p + 1, ed, ml)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, len(arr) - 1, arr)
    print("#{} {}".format(tc,arr[N//2]))
