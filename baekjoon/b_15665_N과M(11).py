def f(k):
    if k==M:
        print(' '.join(map(str,l)))
        return
    else:
        a = 0
        for i in range(N):
            if a != arr[i]:
                l.append(arr[i])
                a = arr[i]
                f(k+1)
                l.pop()



N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0]*N
l = []
arr.sort()

f(0)