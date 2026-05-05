n = 8
board = [input() for _ in range(8)]
placed_coords = []
ans = 0

def place_queen(i):
    global ans

    if i == n:
        ans += 1
        return

    for j in range(n):
        if board[i][j] == "*":
            continue
        for r, c in placed_coords:
            if r == i or c == j or abs(r-i)==abs(c-j):
                break
        else:
            placed_coords.append([i, j])
            place_queen(i+1)
            placed_coords.pop()
place_queen(0)
print(ans)