n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        distance = board[i][j]
        if dp[i][j] == 0:
            continue
        if distance == 0:
            continue
        if i + distance < n:
            dp[i+distance][j] += dp[i][j]
        if j + distance < n:
            dp[i][j+distance] += dp[i][j]
print(dp[-1][-1])