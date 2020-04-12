N = int(input())
friend=[[] for _ in range(N+1)]

while True:
    a,b=map(int,input().split())
    if a==-1:
        break
    friend[a].append(b)
    friend[b].append(a)


Q=[]
nomi = []
cnt=0
Max = 123456789
for i in range(1,N+1):
    Q.append(i)
    visited = [0] * (N + 1)
    visited[i]=1
    while Q:
        a = Q.pop(0)
        for j in friend[a]:
            if visited[j] ==0:
                visited[j]=visited[a]+1
                Q.append(j)

    if max(visited)<Max:
        Max=max(visited)
        cnt=1
        nomi = [i]
    elif max(visited)==Max:
        cnt+=1
        nomi.append(i)
print(Max-1,cnt)

for i in nomi:
    print(i,end=" ")

