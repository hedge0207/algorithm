n, x = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort(reverse=True)
picked = [0] * len(weights)

cnt = 0
ed = len(weights)-1
for st in range(len(weights)):
    if st > ed:
        break
    if weights[st] + weights[ed] <= x:
        ed -= 1
    cnt += 1
print(cnt)