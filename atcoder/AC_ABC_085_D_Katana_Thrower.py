n, h = map(int, input().split())
swords = []
max_a = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > max_a:
        max_a = a
    swords.append([a, b])
swords.sort(key=lambda x:x[1], reverse=True)

ans = 0
i = 0
while h > 0 and i < n and swords[i][1] > max_a:
    a, b = swords[i]
    h -= b
    i += 1
    ans += 1

if h <= 0:
    print(ans)
else:
    if h % max_a != 0:
        ans += 1
    ans += h // max_a
    print(ans)