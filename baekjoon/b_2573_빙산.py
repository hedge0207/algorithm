#시간초과 발생
#빙산이 나누어져있는지 검사할때 탐색함수를 두번돌면 무조건 빙산이 나누어진것이므로
#for문이 끝날때까지 기다리는 것이 아니라 두번째 탐색하려고 진입하는 순간 true를 리턴하고 함수를 종료 시킨다.

import sys
sys.setrecursionlimit(100000)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c,cnt):
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr>=N or nr<0 or nc>=M or nc<0:
            continue
        if arr[nr][nc] == 0 and visited[nr][nc]==0:
            cnt+=1
        if arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc]=1
            dfs(nr,nc,0)

    if cnt>0:
        arr[r][c]-=cnt
        if arr[r][c]<0:
            arr[r][c]=0

def check():
    global ccnt,flag
    for i in range(1,N-1):
        for j in range(1,M-1):
            if arr[i][j] and not visited[i][j]:
                flag=0
                ccnt += 1
                if ccnt>1:
                    return
                visited[i][j]=1
                dfs(i,j,0)

N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

year = 0
while True:
    flag=1
    ccnt=0
    visited = [[0] * M for _ in range(N)]
    check()
    if ccnt>1:
        break
    if flag:
        year=0
        break
    year+=1

print(year)