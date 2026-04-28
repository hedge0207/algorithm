n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: [x[1], x[0]])

ans = 1
prev_ed = times[0][1]
for i in range(1, n):
    st, ed = times[i]
    if prev_ed <= st:
        ans += 1
        prev_ed = ed
print(ans)