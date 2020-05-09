dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    M, N = map(int, input().split())
    mapp = [list(input()) for _ in range(N)]
    visited = [["."] * M for _ in range(N)]
    Q = []
    FQ = []

    for i in range(N):
        for j in range(M):
            if mapp[i][j] == "@":
                Q.append([i, j])
                visited[i][j]=1
            if mapp[i][j] == "*":
                FQ.append([i, j])
                visited[i][j]="*"

    ans = 10 ** 10
    while Q:
        NQ = []
        FNQ = []
        for r,c in FQ:
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=N or nc>=M or nr<0 or nc<0:
                    continue
                if mapp[nr][nc]!="#" and visited[nr][nc]==".":
                    visited[nr][nc]="*"
                    FNQ.append([nr,nc])

        for r, c in Q:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr >= N or nc >= M or nr < 0 or nc < 0:
                    if ans > visited[r][c]:
                        ans = visited[r][c]
                    continue
                if mapp[nr][nc]=="." and visited[nr][nc]==".":
                    visited[nr][nc]=visited[r][c]+1
                    NQ.append([nr,nc])
        Q=NQ
        FQ=FNQ

    if ans==10**10:
        print("IMPOSSIBLE")
    else:
        print(ans)

