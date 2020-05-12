def f(k,c):
    if k==M:
        print(' '.join(map(str,l)))
        return
    a = 0
    for i in range(c,N):
        if visited[i] ==0 and a != arr[i]:
            visited[i]=1
            l.append(arr[i])
            a = arr[i]
            f(k+1,i)
            visited[i]=0
            l.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0]*N
l = []
arr.sort()
f(0,0)