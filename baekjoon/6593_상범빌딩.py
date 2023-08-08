import sys

dl = [-1, 1]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(l, r, c, queue):
    el = er = ec = -1
    while queue:
        new_queue = []
        for pl, pr, pc, cnt in queue:
            for i in dl:
                nl = pl + i
                if nl < 0 or nl >= l:
                    continue

                if building[nl][pr][pc] == "#":
                    continue

                if visited[nl][pr][pc] > cnt + 1:
                    if building[nl][pr][pc] == ".":
                        new_queue.append([nl, pr, pc, cnt + 1])
                    if building[nl][pr][pc] == "E":
                        el, er, ec = nl, pr, pc

                    visited[nl][pr][pc] = cnt + 1

            for i in range(4):
                nr = pr + dr[i]
                nc = pc + dc[i]
                if nr < 0 or nr >= r or nc < 0 or nc >= c:
                    continue

                if building[pl][nr][nc] == "#":
                    continue

                if visited[pl][nr][nc] > cnt + 1:
                    if building[pl][nr][nc] == ".":
                        new_queue.append([pl, nr, nc, cnt + 1])
                    if building[pl][nr][nc] == "E":
                        el, er, ec = pl, nr, nc
                    visited[pl][nr][nc] = cnt + 1

        queue = new_queue
    return el, er, ec


input = sys.stdin.readline
while True:
    l, r, c = map(int, input().split())
    if l == 0:
        break
    building = []
    visited = [[[float("inf")] * c for _ in range(r)] for _ in range(l)]
    queue = []
    for i in range(l):
        floor = []
        for j in range(r):
            row = input().rstrip()
            floor.append(row)
            for k, char in enumerate(row):
                if char == "S":
                    queue.append([i, j, k, 0])
                    visited[i][j][k] = 1
        building.append(floor)
        input()
    el, er, ec = bfs(l, r, c, queue)
    if visited[el][er][ec] < float("inf"):
        print("Escaped in {} minute(s).".format(visited[el][er][ec]))
    else:
        print("Trapped!")