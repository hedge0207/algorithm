N = int(input())

st = 1
ed = 1
sum_ = 1
ans = 0
while st <= ed <= N:
    if sum_ == N:
        ans += 1
        sum_ -= st
        st += 1
        ed += 1
        sum_ += ed
    elif sum_ < N:
        ed += 1
        sum_ += ed
    else:
        sum_ -= st
        st += 1
print(ans)
