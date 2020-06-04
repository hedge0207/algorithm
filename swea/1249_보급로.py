import sys
sys.stdin = open("1249_input.txt", "r")


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def f():
    D = [[0xfffff]*N for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    D[0][0] = 0

    cnt = N*N
    while cnt:
        r,c, MIN = 0,0,0xfffff
        for i in range(N):
            for j in range(N):
                if not visit[i][j] and D[i][j] < MIN:
                    if D[i][j] < MIN:
                        r,c,MIN = i,j,D[i][j]

        visit[r][c] = 1

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if nr>=N or nr<0 or nc>=N or nc<0:
                continue
            if not visit[nr][nc] and D[nr][nc]>D[r][c]+mapp[nr][nc]:
                D[nr][nc] = D[r][c]+mapp[nr][nc]

        cnt -= 1

    print("#{} {}".format(tc,D[N-1][N-1]))


for tc in range(1, int(input()) + 1):
    N = int(input())
    mapp = [list(map(int, input())) for _ in range(N)]
    f()
