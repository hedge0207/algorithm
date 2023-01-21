N = int(input())

is_prime = [0, 0] + [1 for _ in range(N - 1)]

for i in range(2, N + 1):
    if is_prime[i]:
        for j in range(i + i, N + 1, i):
            is_prime[j] = 0

prime = [i for i in range(2, N + 1) if is_prime[i]]

st = 0
ed = 0
sum_ = 2
ans = 0
length = len(prime)
while prime and st <= ed <= length:
    if sum_ == N:
        ans += 1
        sum_ -= prime[st]
        st += 1
    elif sum_ > N:
        sum_ -= prime[st]
        st += 1
    else:
        ed += 1
        if ed == length:
            break
        sum_ += prime[ed]

print(ans)