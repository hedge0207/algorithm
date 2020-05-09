#bfs에서 return을 쓸 때는 조심해자.
import sys
sys.setrecursionlimit(10 ** 6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c,k):
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if nr>=N or nr<0 or nc >=N or nc<0:
            continue
        if maps[nr][nc] == 0:
            maps[r][c] = k
        if maps[nr][nc]==1:
            maps[nr][nc]="L"
            dfs(nr,nc,k)

def bfs(k):
    global Q, Min
    while Q:
        NQ=[]
        for r,c in Q:
            if visited[r][c]>Min:
                break         #break가 아닌 return을 써서 틀림 return할 경우 Q에 요소가 남아있는 상태로 다음 bfs로 넘어가게 된다.
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=N or nr<0 or nc>=N or nc<0:
                    continue
                if maps[nr][nc] !=k and maps[nr][nc] in tk:
                    if Min>visited[r][c]:
                        Min=visited[r][c]
                        break
                if maps[nr][nc]==0 and visited[nr][nc]==0:
                    NQ.append([nr,nc])
                    visited[nr][nc]=visited[r][c]+1
        Q=NQ


N = int(input())
maps=[list(map(int, input().split())) for _ in range(N)]
Min= 987654321

k=1
tk=[]
for i in range(N):
    for j in range(N):
        if maps[i][j]==1:
            k+=1
            tk.append(k)
            maps[i][j]="L"
            dfs(i,j,k)

Q = []
for i in range(N):
    for j in range(N):
        if maps[i][j] in tk:
            visited = [[0] * N for _ in range(N)]
            a = maps[i][j]
            Q.append([i,j])
            visited[i][j] = 1
            bfs(a)

print(Min-1)