import sys
sys.stdin = open("5248_input.txt", "r")

'''
def f(x):
    for i in G[x]:
        if visited[i] == 0:
            visited[i] = 1
            f(i)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    E = list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    
    for i in range(0, len(E), 2):
        s, e = E[i], E[i + 1]
        G[s].append(e)
        G[e].append(s)

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            f(i)
            cnt += 1

    print("#{} {}".format(tc, cnt))
'''

#다른 풀이
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
    if rank[px]>rank[py]:
        p[py]=px
    else:
        p[px]=py
        if rank[px]==rank[py]:
            rank[py]+=1


#union을 통해 노드들을 합한 후 각 집합들의 대표자를 중복 없이 구하면 답을 얻을 수 있다.
for tc in range(1, int(input()) + 1):
    N,M = map(int,input().split())
    p = [0]*(N+1)
    rank = [0]*(N+1)
    E = list(map(int,input().split()))

    for i in range(1,N+1):
        make_set(i)

    for i in range(M):
        s = E[i*2]
        e = E[i*2+1]
        union(s,e)

    result = []
    for i in range(1,len(p)):
        if find_set(p[i]) in result:
            continue
        result.append(find_set(p[i]))  #p는 부모 노드에 대한 정보를 담은 리스트지 대표자에 대한 정보를 담은 리스트가 아니다.
    print("#{} {}".format(tc,len(result)))