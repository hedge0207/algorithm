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
'''


#Prim
# V, E = map(int,input().split())
# adj = [[0]*V for _ in range(V)]
# p = [-1]*V
# key = [0xfffff]*V
# mst = [0]*V
#
# for i in range(E):
#     s,e,c = map(int,input().split())
#     adj[s][e]=c
#     adj[e][s]=c
#
#
# key[0]=0
# cnt= 0
# result = 0
# while cnt<V:
#     Min = 0xfffff
#     u = -1
#     for i in range(V):
#         if not mst[i] and key[i]<Min:
#             Min=key[i]
#             u = i
#     mst[u]=1
#     result+=Min
#     cnt += 1
#
#     for w in range(V):
#         if adj[u][w]>0 and not mst[w] and key[w]>adj[u][w]:
#             key[w]=adj[u][w]
#             p[w]=u
#
# print(result)

V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]

for i in range(E):
    s, e, c, = map(int, input().split())
    adj[s].append([e, c])
    adj[e].append([s, c])

p = [-1]*(V+1)
key = [0xffffffff] * (V + 1)
mst = [0] * (V + 1)

key[1] = 0
mst[1] = 1
start = 1
cnt = 0
result = 0
while True:
    flag = 1
    Min = 0xffffffff
    u = 0

    for i in adj[start]:
        if key[i[0]] > i[1] and not mst[i[0]]:
            key[i[0]] = i[1]
            p[i[0]]=start

    for i in adj[start]:
        if key[i[0]] < Min and mst[i[0]] == 0:
            Min = key[i[0]]
            flag = 0
            u = i[0]

    if flag:
        break

    mst[u] = 1
    result += Min
    cnt += 1

    start = u

print(result)





























