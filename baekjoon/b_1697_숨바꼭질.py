#지나치게 복잡하게 생각해서 오래 걸렸다. 간단하게 생각할 것.

def bfs():
    visited = [0]*100001
    Q = []
    Q.append([N,0])
    while Q:
        NQ = []
        for i in Q:
            x,c=i
            if visited[x]==0:
                visited[x]=1
                if x==K:
                    return c
                if x-1>=0:
                    NQ.append([x-1,c+1])
                if x+1<100001:
                    NQ.append([x+1,c+1])
                if x*2<100001:
                    NQ.append([x*2,c+1])
        Q=NQ

N, K = map(int, input().split())
print(bfs())