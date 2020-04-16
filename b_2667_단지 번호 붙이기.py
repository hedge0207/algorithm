#bfs
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs():
    global cnt,Q
    while Q:
        NQ=[]
        for r,c in Q:
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=N or nr<0 or nc>=N or nc<0:
                    continue
                if complex[nr][nc]==1 and visited[nr][nc]==0:
                    cnt+=1
                    visited[nr][nc]=1
                    NQ.append([nr,nc])    #이 코드에서 NQ.append([nr,nc])가 아닌 Q.append([nr,nc])를 써도 통과가 되었는데 그 이유는 Q에 계속 값이 추가 되면서 for r,c in Q가 계속 돌기 때문이었다.
        Q=NQ                              #만일 len(Q)였다면 for r,c in range(len(Q))로 진입할 당시의 Q의 길이만큼 돌았겠지만 위의 경우에는 Q에 값이 계속 추가되면서 계속 돌았다. 답은 틀리지 않았지만
                                          #이미 처리를 끝낸 Q의 앞부분까지 다시 반복문이 돈 것이기 때문에 시간은 더 오래 걸릴 것이라 생각한다.


N = int(input())
complex = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

tcnt=[]
Q = []
for i in range(N):
    for j in range(N):
        cnt = 1
        if complex[i][j]==1 and visited[i][j]==0:
            Q.append([i,j])
            visited[i][j]=1
            bfs()
            tcnt.append(cnt)

tcnt.sort()
print(len(tcnt))
for i in tcnt:
    print(i)



#dfs
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
#
# N = int(input())
# complex = [list(map(int, input())) for _ in range(N)]
#
# def dfs(r,c):
#     global cnt
#     for i in range(4):
#         nr=r+dr[i]
#         nc=c+dc[i]
#         if nr>=N or nr<0 or nc>=N or nc<0:
#             continue
#         if complex[nr][nc]==1:
#             complex[nr][nc]=-1
#             cnt+=1
#             dfs(nr,nc)
#
#
# tcnt=[]
# for i in range(N):
#     for j in range(N):
#         cnt = 1
#         if complex[i][j]==1:
#             complex[i][j]=-1
#             dfs(i,j)
#             tcnt.append(cnt)
#
#
# tcnt.sort()
# print(len(tcnt))
# for i in tcnt:
#     print(i)