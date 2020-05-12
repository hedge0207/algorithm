def f(k):
    global ans,Sum
    if Sum > M:
        return
    if k==3:
        ans = max(ans,Sum)
        return
    for i in range(N):
        if visited[i]==0:
            visited[i]=1
            Sum+=cards[i]
            f(k+1)
            Sum-=cards[i]
            visited[i]=0


N,M = map(int,input().split())
cards = list(map(int,input().split()))
visited = [0]*N
ans = 0
Sum = 0

f(0)
print(ans)