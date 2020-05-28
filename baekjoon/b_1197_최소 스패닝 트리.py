# Prim
import heapq
V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]

for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])


INF = float('inf')
key = [INF] * (V+1)
mst = [False] * (V+1)

pq = []

key[1] = 1
heapq.heappush(pq,[0,1])

result = 0
while pq:
    k,node = heapq.heappop(pq)

    if mst[node]:
        continue

    mst[node]=True
    result+=k

    for d,w in adj[node]:
        if not mst[d] and key[d]>w:
            key[d]=w
            heapq.heappush(pq,[key[d],d])

print(result)