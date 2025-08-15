n = int(input())
board = []
for _ in range(n):
    board.append(input())

heart_x, heart_y = -1, -1
pieces = []
for y in range(n):
    for x in range(n):
        if board[y][x] == "*":
            if heart_x == -1:
                heart_y, heart_x = y + 1, x
            else:
                if y == heart_y and x == heart_x:
                    continue
                pieces.append([y, x])

l_arm, r_arm, waist, l_leg, r_leg = 0, 0, 0, 0, 0
for piece in pieces:
    y, x = piece
    if y == heart_y:
        if x < heart_x:
            l_arm += 1
        else:
            r_arm += 1
    else:
        if x == heart_x:
            waist += 1
        elif x < heart_x:
            l_leg += 1
        else:
            r_leg += 1

print(heart_y+1, heart_x+1)
print(l_arm, r_arm, waist, l_leg, r_leg)














"""
5
_____
__*__
_***_
__*__
_*_*_
"""