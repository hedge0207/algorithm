#아직도 미완
def f(k,c):
    if k==M:
        for i in l:
            print(i,end=" ")
        print()
    else:
        for i in range(len(arr)):
            if visited[i] ==0 and arr[i] not in vl[k]:
                vl[k].append(arr[i])
                visited[i]=1
                l.append(arr[i])
                f(k+1,i)
                l.pop()



N, M = map(int,input().split())
arr = list(map(int,input().split()))
visited = [0]*N
vl = [[] for _ in range(M)]
print(visited)
arr.sort()

t = []
l=[]
f(0,"C")
print(vl)
