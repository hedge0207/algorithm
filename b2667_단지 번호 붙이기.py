dr = [-1,1,0,0]
dc = [0,0,-1,1]

N = int(input())
complex = [list(map(int, input())) for _ in range(N)]

def dfs(r,c):
    global cnt
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if nr>=N or nr<0 or nc>=N or nc<0:
            continue
        if complex[nr][nc]==1:
            complex[nr][nc]=-1
            cnt+=1
            dfs(nr,nc)


tcnt=[]
for i in range(N):
    for j in range(N):
        cnt = 1
        if complex[i][j]==1:
            complex[i][j]=-1
            dfs(i,j)
            tcnt.append(cnt)


tcnt.sort()
print(len(tcnt))
for i in tcnt:
    print(i)
