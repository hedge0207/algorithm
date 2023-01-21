N, K = map(int, input().split())
temp = list(map(int, input().split()))

st = 0
ed = K - 1
sum_temp = sum(temp[st:ed + 1])
max_sum_temp = sum_temp
while 1:
    ed += 1
    if ed == N:
        break
    sum_temp += temp[ed] - temp[st]
    st += 1

    if max_sum_temp < sum_temp:
        max_sum_temp = sum_temp

print(max_sum_temp)
