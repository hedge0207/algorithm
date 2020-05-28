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
    px=find_set(x)
    py=find_set(y)
    if rank[px]<rank[py]:
        p[px]=py
    else:
        p[py]=px
        if rank[px]==rank[py]:
            rank[px]+=1


V = int(input())
E = int(input())
edges = [list(map(int,input().split())) for _ in range(E)]
edges.sort(key=lambda x:x[2])

p = [0]*(V+1)
rank = [0]*(V+1)
for i in range(1,V+1):
    make_set(i)

cnt = 0
result = 0
for i in range(E):
    s,e,c=edges[i][0],edges[i][1],edges[i][2]
    if find_set(s)==find_set(e):
        continue

    result+=c
    cnt+=1
    union(s,e)
    if cnt==V-1:
        break

print(result)