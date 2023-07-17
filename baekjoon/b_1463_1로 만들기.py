N = int(input())
table = [0] * (N + 1)

for i in range(2, N + 1):
    cnt = table[i - 1] + 1
    if i % 3 == 0:
        cnt = min(cnt, table[i // 3] + 1)
    if i % 2 == 0:
        cnt = min(cnt, table[i // 2] + 1)
    table[i] = cnt

print(table[N])