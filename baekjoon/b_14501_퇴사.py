def recur(k, remain, sum_):
    global result
    if k == N:
        if sum_ > result:
            result = sum_
        return

    if remain <= 0:
        t, p = table[k]
        if t <= N - k:
            recur(k + 1, t - 1, sum_ + p)
    recur(k + 1, remain-1, sum_)


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
result = 0
recur(0, 0, 0)
print(result)
