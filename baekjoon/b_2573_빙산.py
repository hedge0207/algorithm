dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check():


def dfs(r,c):
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr>=N or nr<0 or nc>=M or nc<0:
            continue
        if not visited[nr][nc] and arr[nr][nc]:
            visited[nr][nc]=1
            dfs(nr,nc)
        if arr[nr][nc]==0 and arr[r][c]!=0:
            arr[r][c]-=1


N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

while True:
    if check():
        break
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j]:
                visited[i][j]=1
                dfs(i,j)
print(arr)
