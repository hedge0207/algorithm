# 에라토스테네스의 체
N = 1000000
r = int(N ** 0.5)
prime = [0] * (N + 1)

for i in range(2, r):
    if prime[i]:
        continue
    for j in range(i, N + 1, i):
        if i == j:
            continue
        if prime[j] == 0:
            prime[j] = 1

for i in range(len(prime)):
    if i == 0 or i == 1:
        continue
    if prime[i] == 0:
        print(i, end=" ")
