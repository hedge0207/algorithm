import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]

dr=[-1,1,0,0]
dc=[0,0,-1,1]

def dfs(r,c):
    global cnt
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if nr < 0 or nr >= n or nc <0 or nc>=m:
            continue
        if paint[nr][nc]==1:
            paint[nr][nc]=2
            cnt+=1
            dfs(nr,nc)
    return cnt

pcnt = 0
cntl = []
for i in range(n):
    for j in range(m):
        cnt=1
        if paint[i][j] == 1:
            paint[i][j]=2
            cntl+=[dfs(i,j)]
            pcnt+=1
if pcnt != 0:
    print(pcnt)
    print(max(cntl))
else:
    print(pcnt)
    print(0)




