import sys
sys.stdin = open("5251_input.txt", "r")

for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    for i in range(E):
        s,e,c = map(int,input().split())
        G[s]=[e,c]
        G[e]=[s,c]

    key = [0xffffff]*(V+1)
    mst = [0]*(V+1)
    key[0] = 0

    cnt = 0
    result = 0
    while cnt<V+1:
        Min = 0xffffff
        u = -1

        for i in range(V+1):
            if not mst and Min>key[i]:
                Min = key[i]
                u = i

        mst[u]=1
        result+=Min

        for v,w in G[u]:
            if key[v]>key[u]+w:
                key[v]=key[u]+w

    print(result)


