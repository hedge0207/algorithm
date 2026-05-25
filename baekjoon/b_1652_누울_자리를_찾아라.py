n = int(input())
room = [input() for _ in range(n)]

ans_row = 0
ans_col = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if room[i][j] == ".":
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            ans_row += 1

    cnt = 0
    for j in range(n):
        if room[j][i] == ".":
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            ans_col += 1

print(ans_row, ans_col)