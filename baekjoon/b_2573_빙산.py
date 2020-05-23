dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    cnt= 0
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr>=N or nr<0 or nc>=M or nc<0:
            continue
        if arr[nr][nc] == 0 and arr[r][c] != 0:
            cnt+=1
        if not visited[nr][nc] and arr[nr][nc]:
            visited[nr][nc]=1
            dfs(nr,nc)

N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


for i in range(2):
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j]:
                visited[i][j]=1
                dfs(i,j)
    print(arr)
