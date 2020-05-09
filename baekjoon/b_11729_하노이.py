def h(n, st, ed):
    global cnt
    if n < 2:
        cnt += 1
        a.append([st, ed])
        return
    mi = 6 - st - ed
    h(n - 1, st, mi)
    cnt += 1
    a.append([st, ed])
    h(n - 1, mi, ed)
    return

cnt = 0
n = int(input())
a = []
h(n, 1, 3)
print(cnt)

for i in range(len(a)):
    print(a[i][0], a[i][1])
