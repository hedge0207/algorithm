N = int(input())
G = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(N-1):
    u,v = map(int,input().split())
    G[v].append(u)
    G[u].append(v)

edges = []
Q = [[0,1]]
while Q:
    flag = 0
    NQ = []
    for i in Q:
        p,node = i
        for i in G[node]:
            if visited[node]==0:
                flag = 1
                if p==i:
                    continue
                NQ.append([node,i])
                edges.append([node,i])
        if flag:
            visited[node]=1
    Q = NQ

parent = [0]*(N+1)
for i in edges:
    p,c = i[0],i[1]
    parent[c]=p

for i in range(2,len(parent)):
    print(parent[i])





