import sys


input = sys.stdin.readline
N, K = map(int, input().split())
tmp_ice = {}
for _ in range(N):
    i, c = map(int, input().split())
    tmp_ice[c] = i

max_coord = max(tmp_ice.keys())
ice = []
for i in range(max_coord + 1):
    is_exist = tmp_ice.get(i)
    if is_exist:
        ice.append(is_exist)
    else:
        ice.append(0)

result = -1
range_ = K * 2 + 1
st = 0
ed = -1
sum_ = 0

while True:
    if ed - st + 1 == range_:
        sum_ -= ice[st]
        st += 1
    ed += 1
    sum_ += ice[ed]

    result = max(sum_, result)

    if ed == max_coord:
        break

print(result)