import sys
input = sys.stdin.readline

while 1:
    N, M = list(map(int, input().split()))

    if N == 0 and M == 0:
        break

    cds = list(map(int, [input() for _ in range(N + M)]))

    p1 = 0
    p2 = N

    ans = 0
    while p1 < N and p2 < N + M:
        if cds[p1] == cds[p2]:
            ans += 1
            p1 += 1
            p2 += 1
        elif cds[p1] > cds[p2]:
            p2 += 1
        else:
            p1 += 1

    print(ans)