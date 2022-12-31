N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
st = 0
ed = 1
sum_ = lst[st]
while 1:
    if sum_ == M:
        ans += 1
        sum_ -= lst[st]
        st += 1
    elif sum_ > M:
        sum_ -= lst[st]
        st += 1
    else:
        if ed == N:
            break
        sum_ += lst[ed]
        ed += 1
print(ans)
