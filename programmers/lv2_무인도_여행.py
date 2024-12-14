dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(queue, n, m, maps, visited):
    stock = 0
    while queue:
        new_queue = []
        for x, y in queue:
            stock += int(maps[x][y])
            for i in range(4):
                nx = x + dr[i]
                ny = y + dc[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == "X":
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = 1
                new_queue.append([nx, ny])
        queue = new_queue
    return stock


def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visited[i][j]:
                continue
            if maps[i][j] != "X":
                visited[i][j] = 1
                answer.append(bfs([[i, j]], n, m, maps, visited))

    return sorted(answer) if answer else [-1]