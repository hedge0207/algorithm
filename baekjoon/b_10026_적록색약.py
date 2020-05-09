import sys
sys.setrecursionlimit(100000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def no(r, c, l):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] == l:
            arr[nr][nc] = 0
            no(nr, nc, l)




N = int(input())
arr = [list(input()) for _ in range(N)]
arr2=[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        arr2[i][j]=arr[i][j]



cnt=0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            cnt+=1
            no(i, j, arr[i][j])

for i in range(N):
    for j in range(N):
        arr[i][j]=arr2[i][j]



for i in range(N):
    for j in range(N):
        if arr[i][j]=="G":
            arr[i][j]="R"

cntt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            cntt+=1
            no(i, j, arr[i][j])
print(cnt, cntt)