X = input()
Y = input()
N = len(X)
M = len(Y)

table = [[0]*(M+1) for _ in range(N+1)]

ans = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if X[i-1] == Y[j-1]:
            table[i][j] = table[i-1][j-1] + 1
            ans = max(table[i][j], ans)

print(ans)