n = int(input())
commands = input()
board = [["."] * n for _ in range(n)]
move_per_command = {"D": [1, 0], "U": [-1, 0], "R": [0, 1], "L": [0, -1]}
cur = [0, 0]
for command in commands:
    move = move_per_command[command]
    nr, nc = cur[0] + move[0], cur[1] + move[1]
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        continue
    mark = "-"
    if command in ["D", "U"]:
        mark = "|"
    board[cur[0]][cur[1]] = "+" if board[cur[0]][cur[1]] != "." and board[cur[0]][cur[1]] != mark else mark
    cur = [nr, nc]
    board[cur[0]][cur[1]] = "+" if board[cur[0]][cur[1]] != "." and board[cur[0]][cur[1]] != mark else mark
for row in board:
    print("".join(row))