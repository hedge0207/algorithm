import sys
sys.stdin = open("1238_input.txt", "r")

def bfs(s):
    Q = []
    Q.append(s)
    visited[s]=1
    ans = []
    while Q:
        NQ = []
        for i in Q:
            for j in range(len(connect[i])):
                if not visited[j] and connect[i][j]:
                    visited[j]=1
                    NQ.append(j)
        Q = NQ
        if NQ:
            ans = NQ
    return ans


for tc in range(1,11):
    N,S = map(int,input().split())
    contact = list(map(int,input().split()))
    connect = [[0]*101 for _ in range(101)]
    visited=[0]*101
    for i in range(0,N,2):
        connect[contact[i]][contact[i+1]] = 1

    ans = bfs(S)
    print("#{} {}".format(tc,max(ans)))