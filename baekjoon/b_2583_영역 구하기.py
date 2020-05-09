import sys
sys.setrecursionlimit(1000000)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global cnt
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= M or nr < 0 or nc >= N or nc < 0:
            continue
        if arr[nr][nc]==0:
            arr[nr][nc]=2
            cnt+=1
            dfs(nr,nc)


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]


for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(M):
        for j in range(N):
            if r1<= i < r2 and c1<=j<c2:
                arr[i][j]=1



cntt=[]
for i in range(M):
    for j in range(N):
        cnt = 1
        if arr[i][j]==0:
            arr[i][j]=2
            dfs(i,j)
            cntt+=[cnt]

print(len(cntt))

def merge(l1,l2):
    i=0
    j=0
    result=[]
    while i<len(l1) and j <len(l2):
        if l1[i]>l2[j]:
            result.append(l2[j])
            j+=1
        else:
            result.append(l1[i])
            i+=1

    if len(l1)==i:
        result+=l2[j:]
    if len(l2)==j:
        result+=l1[i:]

    return result

def msort(ml):
    if len(ml)<2:
        return ml
    ll = ml[:len(ml)//2]
    rl = ml[len(ml) // 2:]

    return merge(msort(ll),msort(rl))

for i in msort(cntt):
    print(i, end= " ")