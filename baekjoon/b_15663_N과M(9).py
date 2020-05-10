#미완
def f(k):
    global t
    if k==M:
        for i in l:
            print(i,end=" ")
        print()
    else:
        for i in range(len(arr)):
            if visited[i]:
                continue
            else:
                visited[i]=1
                l.append(arr[i])
                f(k+1)
                visited[i]=0
                l.pop()

N, M = map(int,input().split())
arr = list(map(int,input().split()))
visited= [0]*(N+1)
arr.sort()
t = []

l=[]
f(0)

