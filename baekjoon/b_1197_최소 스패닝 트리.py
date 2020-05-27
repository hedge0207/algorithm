V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    s, e, c = map(int, input().split())
    adj[s][e] = c
    adj[e][s] = c


INF = float('inf')
key = [INF] * (V+1)
mst = [False] * (V+1)

key[1] = 0
cnt = 0
result = 0
while cnt < V:

    Min = INF
    u = -1

    for i in range(1,V+1):
        if not mst[i] and key[i] < Min:
            Min = key[i]
            u = i


    mst[u] = True
    result += Min
    cnt += 1

    for w in range(1,V+1):
        if not mst[w] and key[w] > adj[u][w]:
            key[w] = adj[u][w]

print(result)
