n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
used = [0] * (n+1)
def recur(d, num):
    global ans
    if d == 0:
        if a < num < b:
            ans += 1
        return

    for i in range(1, n+1):
        if used[i]:
            continue

        used[i] = 1
        recur(d-1, num + [i])
        used[i] = 0

recur(n, [])
print(ans)