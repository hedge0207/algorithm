from enum import Enum
from collections import deque

class MapChar(Enum):
    START = "S"
    EXIT = "E"
    LEVER = "L"
    O = "O"
    X = "X"


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, maps):
    n = len(maps)
    m = len(maps[0])
    distances = [[float("inf")] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    find_start = False
    find_exit = False

    while queue:
        if find_exit and find_start:
            break
        x, y, distance = queue.popleft()
        distances[x][y] = distance

        if maps[x][y] == MapChar.START.value:
            find_start = True

        if maps[x][y] == MapChar.EXIT.value:
            find_exit = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if maps[nx][ny] == MapChar.X.value:
                continue

            if visited[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            queue.append([nx, ny, distance + 1])
    return distances


def solution(maps):
    start_x, start_y, exit_x, exit_y = -1, -1, -1, -1
    distances = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == MapChar.LEVER.value:
                queue = deque()
                queue.append([i, j, 0])
                distances = bfs(queue, maps)
            elif maps[i][j] == MapChar.START.value:
                start_x, start_y = i, j
            elif maps[i][j] == MapChar.EXIT.value:
                exit_x, exit_y = i, j

    if distances[start_x][start_y] == float("inf") or distances[exit_x][exit_y] == float("inf"):
        return -1

    return distances[start_x][start_y] + distances[exit_x][exit_y]


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
