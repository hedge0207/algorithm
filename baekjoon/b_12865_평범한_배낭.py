n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

result = 0
table = [[0] * (k+1) for _ in range(n+1)]
bag_weight = 0
for i in range(1, n+1):
    w, v = items[i - 1]
    for j in range(k+1):
        if w <= j:
            table[i][j] = max(table[i-1][j], table[i-1][j-w] + v)
        else:
            table[i][j] = table[i-1][j]
        result = max(table[i][j], result)

print(result)