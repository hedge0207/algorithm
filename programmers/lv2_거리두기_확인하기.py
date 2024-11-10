from enum import Enum


class Mark(Enum):
    CANDIDATE = "P"
    EMPTY = "O"
    PARTITION = "X"


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(place, visited, r, c, d, k):
    if d == k:
        return

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr <= -1 or nc <= -1 or nr >= 5 or nc >= 5:
            continue

        if visited[nr][nc]:
            continue

        if place[nr][nc] == Mark.PARTITION.value:
            continue
        elif place[nr][nc] == Mark.CANDIDATE.value:
            return True
        else:
            if dfs(place, visited, nr, nc, d + 1, k):
                return True


def is_valid_distance(place):
    N = 5

    for i in range(N):
        for j in range(N):
            if place[i][j] == Mark.CANDIDATE.value:
                visited = [[0] * 5 for _ in range(N)]
                if dfs(place, visited, i, j, 0, 2):
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        answer.append(1 if is_valid_distance(place) else 0)
    return answer
