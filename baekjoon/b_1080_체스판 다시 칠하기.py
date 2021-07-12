def re_color(start_r, start_c):
    for color in ['W', 'B']:
        cnt = 0
        for r in range(start_r, start_r + 8):
            if r != start_r:
                if color == "W":
                    color = "B"
                else:
                    color = "W"
            for c in range(start_c, start_c + 8):
                if board[r][c] != color:
                    cnt += 1
                if color == "W":
                    color = "B"
                else:
                    color = "W"

        cnt_lst.append(cnt)


N, M = map(int, input().split())
board = [input() for _ in range(N)]
cnt_lst = []

for i in range(N):
    if i + 7 >= N:
        break
    for j in range(M):
        if j + 7 > M:
            break
        if i + 7 < N and j + 7 < M:
            re_color(i, j)

print(min(cnt_lst))