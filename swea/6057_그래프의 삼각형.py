import sys
sys.stdin=open("6057_input.txt","r")

def dfs(s,e,l):
    global cnt
    if len(l)==3:
        if s in G[e]:
            cnt+=1
        return
    for i in G[e]:
        if i not in l:
            l.append(i)
            dfs(s,i,l)
            l.pop()


for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    G = [[] for _ in range(N+1)]
    for i in range(M):
        s,e = map(int,input().split())
        G[s].append(e)
        G[e].append(s)

    cnt=0
    tl = []
    for i in range(1,len(G)):
        dfs(i,i,[i])
    print("#{} {}".format(tc,cnt//6))
