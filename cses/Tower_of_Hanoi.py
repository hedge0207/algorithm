n = int(input())

ans_cnt = 0
path = []

def recur(l, m, r, cnt):
    global ans_cnt

    if cnt > n:
        return
    recur(l, r, m, cnt+1)

    if cnt > 0:
        ans_cnt += 1
        path.append([l, m])
        recur(r, m, l, cnt+1)

recur(1, 2, 3, 0)
print(ans_cnt)
for i, j in path:
    print(i, j)