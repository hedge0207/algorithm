board_size = 5
position_per_num = {}

for i in range(5):
    for j, num in enumerate(input().split()):
        position_per_num[num] = [i, j]

called_numbers = []
for _ in range(5):
    called_numbers += input().split()

rows = {i:0 for i in range(board_size)}
cols = {i:0 for i in range(board_size)}
positive_diagonal = 0
negative_diagonal = 0

ans = 0
num_lines = 0
for i, num in enumerate(called_numbers):
    x, y = position_per_num[num]
    rows[x] += 1
    if rows[x] == board_size:
        num_lines += 1
    cols[y] += 1
    if cols[y] == board_size:
        num_lines += 1
    if x == y:
        negative_diagonal += 1
        if negative_diagonal == board_size:
            num_lines += 1
    if x + y == board_size - 1:
        positive_diagonal += 1
        if positive_diagonal == board_size:
            num_lines += 1
    if num_lines >= 3:
        ans = i + 1
        break

print(ans)


























"""
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
11 16 6 19 22
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
11 12 2 24 10
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
18 14 5 1 11
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
22 4 5 3 10
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
14 5 11 22 4
7 24 21 8 1
19 10 20 23 17
13 18 9 15 6
16 3 12 2
"""