N, M = list(map(int, input().split()))
cds = list(map(int, [input() for _ in range(N + M)]))
end = input()

p1 = 0
p2 = M

ans = 0
while p1 < M and p2 < N + M:
    if cds[p1] == cds[p2]:
        ans += 1
    p1 += 1
    p2 += 1

print(ans)