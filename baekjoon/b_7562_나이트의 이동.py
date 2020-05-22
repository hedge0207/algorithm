dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]


def bfs():
    Q = []
    Q.append([sr, sc])
    visited[sr][sc] = 1
    while Q:
        NQ = []
        for i in Q:
            r, c, = i
            if r == er and c == ec:
                return visited[r][c]-1
            for j in range(8):
                nr = r + dr[j]
                nc = c + dc[j]
                if nr >= N or nr < 0 or nc >= N or nc < 0:
                    continue
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    NQ.append([nr, nc])
        Q = NQ


for tc in range(int(input())):
    N = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    visited = [[0] * N for _ in range(N)]

    print(bfs())
