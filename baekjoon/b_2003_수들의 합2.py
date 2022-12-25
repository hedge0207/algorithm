N, M = map(int, input().split())
arr = list(map(int, input().split()))

st = 0
ed = st + 1

cnt = 0
while st < ed:
    if ed == N-1:
        st += 1
    sum_ = sum(arr[st:ed])
    if sum_ == M:
        cnt += 1
        ed += 1
    elif sum_ > M:
        st += 1