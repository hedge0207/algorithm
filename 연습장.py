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
'''


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
