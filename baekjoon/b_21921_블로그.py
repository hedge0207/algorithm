N, X = map(int, input().split())
num_user = list(map(int, input().split()))

st = 0
ed = X - 1
sum_user = sum(num_user[st:ed+1])
max_num_user = sum_user
cnt = 1
while 1:
    ed += 1
    if ed == N:
        break
    sum_user += num_user[ed] - num_user[st]
    st += 1

    if max_num_user < sum_user:
        max_num_user = sum_user
        cnt = 1
    elif max_num_user == sum_user:
        cnt += 1

if max_num_user:
    print(max_num_user)
    print(cnt)
else:
    print("SAD")
