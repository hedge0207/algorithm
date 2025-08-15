n = int(input())
towers = list(map(int, input().split()))

broken = [0 for _ in range(len(towers))]
ans = 1
for i in range(1, n):
    if towers[i-1] <= towers[i]:
        ans += 1

print(ans)