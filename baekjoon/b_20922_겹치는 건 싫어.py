N, K = map(int, input().split())
sequence = list(map(int, input().split()))

st = 0
ed = 0
ans = 0
num_cnt = {}
lst = []
while st <= ed < N:
    num = sequence[ed]
    if num_cnt.get(num) is None:
        num_cnt[num] = 1
        lst.append(num)
        ed += 1
    else:
        if num_cnt.get(num) < K:
            num_cnt[num] += 1
            lst.append(num)
            ed += 1
        else:
            ans = max(ans, len(lst))
            lst = lst[lst.index(num)+1:]
            num_cnt = {}
            for i in lst:
                if num_cnt.get(i):
                    num_cnt[i] += 1
                else:
                    num_cnt[i] = 1
            st += 1

ans = max(ans, len(lst))

print(ans)
