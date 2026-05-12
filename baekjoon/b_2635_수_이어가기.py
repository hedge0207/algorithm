n = int(input())

ans = []
for i in range(1, n+1):
    candidate = [n, i]
    while 1:
        num = candidate[-2] - candidate[-1]
        if  num < 0:
            break
        candidate.append(num)
    if len(ans) < len(candidate):
        ans = candidate

print(len(ans))
for num in ans:
    print(num, end=" ")