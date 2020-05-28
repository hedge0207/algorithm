'''
#그래프
,E = map(int,input().split())
G = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    u,v = map(int,input().split())
    G[u][v]=1
    G[v][u]=1

print(G)

V,E = map(int,input().split())
G = [[] for _ in range(V+1)]

for _ in range(E):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

print(G)



#disjoint_set
def make_set(x):
    p[x]=x

def find_set(x):
    if p[x]==x:
        return x
    else:
        return find_set(p[x])

def union(x,y):
    p[find_set(y)]=find_set(x)


N = 8
p = [0]*(N+1)
for i in range(1,N+1):
    make_set(i)

union(7,8)
union(6,7)
union(5,6)
union(4,5)
union(3,4)
union(2,3)
union(1,2)
print(p)
print(find_set(6))



#disjoint_set_rank
def make_set(x):
    p[x]=x

def find_set(x):
    if p[x]==x:
        return x
    else:
        p[x]=find_set(p[x])
        return p[x]

def union(x,y):
    px=find_set(x)
    py=find_set(y)
    if rank[py]>rank[px]:
        p[px]=py
    else:
        p[py]=px
        if rank[px]==rank[py]:
            rank[px]+=1


N = 8
p = [0]*(N+1)
rank = [0]*(N+1)
for i in range(1,N+1):
    make_set(i)

union(7,8)
union(6,7)
union(5,6)
union(4,5)
union(3,4)
union(2,3)
union(1,2)
print(p)
print(find_set(6))




#Prim
V, E = map(int,input().split())
adj = [[0]*V for _ in range(V)]
p = [-1]*V
key = [0xfffff]*V
mst = [0]*V

for i in range(E):
    s,e,c = map(int,input().split())
    adj[s][e]=c
    adj[e][s]=c


key[0]=0
cnt= 0
result = 0
while cnt<V:
    Min = 0xfffff
    u = -1
    for i in range(V):
        if not mst[i] and key[i]<Min:
            Min=key[i]
            u = i
    mst[u]=1
    result+=Min
    cnt += 1

    for w in range(V):
        if adj[u][w]>0 and not mst[w] and key[w]>adj[u][w]:
            key[w]=adj[u][w]
            p[w]=u

print(result)


#Prim_priorityqueue
import heapq

V,E = map(int,input().split())
adj = [[] for _ in range(V)]

for i in range(E):
    s,e,c = map(int,input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])

INF = float('inf')
key = [INF] * V
mst = [False] * V
pq = []

key[0] = 0
heapq.heappush(pq,[0,0])

result = 0

while pq:
    k,node = heapq.heappop(pq)

    if mst[node]:
        continue

    mst[node] = True
    result += k

    for d,w in adj[node]:
        if not mst[d] and key[d]>w:
            key[d]=w
            heapq.heappush(pq,[key[d],d])

print(result)


#KRUSKAL
def make_set(x):
    p[x]=x

def find_set(x):
    if p[x]==x:
        return x
    else:
        p[x]=find_set(p[x])
        return p[x]

def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if rank[py]>rank[px]:
        p[px]=py
    else:
        p[py]=px
        if rank[px]==rank[py]:
            rank[px]+=1


V, E = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(E)]

edges.sort(key=lambda x: x[2])

p = [0]*V
rank = [0]*V
for i in range(V):
    make_set(i)

cnt = 0
result = 0
mst = []
for i in range(E):
    s,e,c = edges[i][0],edges[i][1],edges[i][2]
    if find_set(s)==find_set(e):
        continue
    result+=c
    mst.append(edges[i])
    union(s,e)
    cnt+=1
    if cnt==V-1:
        break

print(result)
'''
# import sys
#
# sys.stdin = open("1244_input.txt", "r")
#
# for tc in range(1, int(input()) + 1):
#     tmp1, tmp2 = input().split()
#     Max = -1
#     n = list(map(int, tmp1))
#     c = int(tmp2)
#
#     ans = 0
#     for i in range(len(n) - 1):
#         for j in range(i + 1, len(n)):
#             n[i], n[j] = n[j], n[i]
#             print(n)
#             n[i], n[j] = n[j], n[i]

# def f(k,c):
#     if k==c:
#         print(arr)
#         return
#     for i in a:
#         arr.append(i)
#         f(k+1,c)
#         arr.pop()
#
# arr = []
# a = [1,2,3]
# f(0,3)

# def f(k,c):
#     if k==c:
#         print(arr)
#         return
#     for i in range(len(a)):
#         if not visited[i]:
#             visited[i]=1
#             arr.append(a[i])
#             f(k+1,c)
#             arr.pop()
#
# arr = []
# a = [1,2,3]
# visited = [0]*3
# f(0,3)


a = 2
print(a==1)












