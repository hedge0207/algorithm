def is_end(board, char):
    for row in board:
        if row == [char, char, char]:
            return True

    for col in range(3):
        if [board[row][col] for row in range(3)] == [char, char, char]:
            return True

    if [board[0][0], board[1][1], board[2][2]] == [char, char, char]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [char, char, char]:
        return True

    return False


def solution(board):
    board = [list(row) for row in board]

    num_o, num_x = 0, 0
    for row in board:
        for c in row:
            if c == 'O':
                num_o += 1
            if c == 'X':
                num_x += 1

    if not (num_o == num_x or num_o == num_x + 1):
        return 0

    if is_end(board, 'O') and is_end(board, 'X'):
        return 0

    if is_end(board, 'O') and num_o != num_x + 1:
        return 0

    if is_end(board, 'X') and num_o != num_x:
        return 0

    return 1