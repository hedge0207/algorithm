N, K = map(int, input().split())
R = int(N ** 0.5)
prime = [0] * (N + 1)

ans = 0
flag = 0
cnt = 1
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if prime[j] == 0:
            if cnt == K:
                ans = j
                flag = 1
                break
            prime[j] = cnt
            cnt += 1
    if flag:
        break

print(ans)
